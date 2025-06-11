from fastapi import FastAPI, HTTPException
from app.model import recommender

app = FastAPI(title="Go-UMKM Recommendation API")

# Load model saat startup
@app.on_event("startup")
def load():
    recommender.load_model()

@app.get("/")
def root():
    return {"message": "Go-UMKM Recommendation API is running."}

@app.get("/recommend/{user_id}")
def recommend(user_id: str, k: int = 5):
    try:
        results = recommender.get_recommendations(user_id=user_id, k=k)
        if isinstance(results, dict) and "error" in results:
            raise HTTPException(status_code=404, detail=results["error"])
        return {"user_id": user_id, "recommendations": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
