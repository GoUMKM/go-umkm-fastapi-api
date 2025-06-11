import joblib
import tensorflow as tf
import numpy as np

preprocessor = None
interpreter = None

def load_model():
    global preprocessor, interpreter
    preprocessor = joblib.load("app/model/artifacts/preprocessor.joblib")
    
    # Load TFLite model menggunakan interpreter
    interpreter = tf.lite.Interpreter(model_path="app/model/artifacts/similarity_model.tflite")
    interpreter.allocate_tensors()

def get_recommendations(user_id: str):
    if interpreter is None:
        return {"error": "Model not loaded"}
    
    # Contoh input dummy, sesuaikan dengan input modelmu
    # Biasanya harus pakai preprocessor untuk olah input dulu
    input_data = np.array([0.0], dtype=np.float32)  # ganti sesuai input
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)
    # Run inference
    interpreter.invoke()
    # Ambil output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    # Contoh output dummy, sesuaikan dengan keluaran model
    recommendations = [f"user_{i}" for i in range(5)]
    return {"recommendations": recommendations}
