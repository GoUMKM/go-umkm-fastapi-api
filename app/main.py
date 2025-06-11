from fastapi import FastAPI
from app.model.recommender import load_model, get_recommendations
from app.schemas.request_response import RecommendationRequest

app = FastAPI()

@app.on_event("startup")
def startup_event():
    load_model()

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}

@app.post("/recommend")
def recommend(data: RecommendationRequest):
    return get_recommendations(data.user_id)

