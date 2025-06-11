import joblib
import tflite_runtime.interpreter as tflite
import os

preprocessor = None
interpreter = None

def load_model():
    global preprocessor, interpreter
    preprocessor = joblib.load("app/model/artifacts/preprocessor.joblib")
    interpreter = tflite.Interpreter(model_path="app/model/artifacts/similarity_model.tflite")
    interpreter.allocate_tensors()

def get_recommendations(user_id: str):
    if interpreter is None:
        return {"error": "Model not loaded"}

    # Contoh inferensi sederhana
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # TODO: siapkan input sesuai input_details, lalu set input tensor
    # interpreter.set_tensor(input_details[0]['index'], input_data)
    # interpreter.invoke()
    # output_data = interpreter.get_tensor(output_details[0]['index'])

    # Placeholder return
    return {"recommendations": [f"user_{i}" for i in range(5)]}
