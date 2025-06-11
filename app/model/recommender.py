import joblib
import tensorflow as tf
import os

preprocessor = None
similarity_model = None

def load_model():
    global preprocessor, similarity_model
    preprocessor = joblib.load("app/model/artifacts/preprocessor.joblib")
    similarity_model = tf.keras.models.load_model("app/model/artifacts/similarity_model.h5")

def get_recommendations(user_id: str):
    # Placeholder logic, ganti sesuai kebutuhan
    if similarity_model is None:
        return {"error": "Model not loaded"}
    return {"recommendations": [f"user_{i}" for i in range(5)]}
