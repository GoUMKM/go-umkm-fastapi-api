import joblib
import tflite_runtime.interpreter as tflite
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

# Global variables
preprocessor = None
interpreter = None
users_df = None
umkm_df = None
investor_df = None
cosine_sim = None
embeddings = None

def load_model():
    global preprocessor, interpreter, users_df, umkm_df, investor_df, cosine_sim, embeddings

    # Load preprocessor
    preprocessor = joblib.load("app/model/artifacts/preprocessor.joblib")

    # Load user data
    umkm_df = pd.read_csv("app/model/data/umkm_data.csv")
    investor_df = pd.read_csv("app/model/data/investor_data.csv")
    users_df = pd.concat([
        umkm_df.drop(columns=["umkm_id"]),
        investor_df.drop(columns=["investor_id"])
    ], ignore_index=True)

    # Preprocess data
    features = preprocessor.transform(users_df)
    features_dense = features.toarray() if hasattr(features, "toarray") else features

    # Load tflite model
    interpreter = tflite.Interpreter(model_path="app/model/artifacts/similarity_model.tflite")
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Generate embeddings
    emb_list = []
    for i in range(features_dense.shape[0]):
        input_data = np.array([features_dense[i]], dtype=np.float32)
        interpreter.set_tensor(input_details[0]["index"], input_data)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]["index"])
        emb_list.append(output[0])
    
    embeddings = np.array(emb_list)
    normalized_embeddings = normalize(embeddings)
    cosine_sim = np.dot(normalized_embeddings, normalized_embeddings.T)

def get_profile_type(user_id):
    if user_id in umkm_df['user_id'].values:
        return 'umkm'
    elif user_id in investor_df['user_id'].values:
        return 'investor'
    else:
        return None

def get_recommendations(user_id: str, k: int = 5):
    global cosine_sim, users_df, umkm_df, investor_df

    if cosine_sim is None:
        return {"error": "Model not loaded"}

    user_type = get_profile_type(user_id)
    if user_type is None:
        return {"error": "User ID not found"}

    try:
        idx = users_df[users_df["user_id"] == user_id].index[0]
    except IndexError:
        return {"error": "User ID not in user list"}

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:k+1]  # exclude self

    user_indices = [i[0] for i in sim_scores]
    user_ids = users_df.iloc[user_indices]["user_id"].tolist()
    scores = [float(i[1]) for i in sim_scores]

    if user_type == "umkm":
        result = investor_df[investor_df["user_id"].isin(user_ids)].copy()
    else:
        result = umkm_df[umkm_df["user_id"].isin(user_ids)].copy()

    result = result.merge(pd.DataFrame({
        "user_id": user_ids,
        "similarity_score": scores
    }), on="user_id")

    return result.to_dict(orient="records")
