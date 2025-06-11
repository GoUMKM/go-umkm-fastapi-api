from fastapi import FastAPI
from app.schemas.request_response import RecommendRequest
from app.model.recommender import get_recommendations  # pastikan fungsi ini ada

app = FastAPI()

@app.post("/recommend")
def recommend(request: RecommendRequest):
    try:
        result = get_recommendations(
            user_id=request.user_id,
            cosine_sim=cosine_sim,
            users_df=users_df,
            umkm_data=umkm_df,
            investor_data=investor_df,
            k=request.top_k
        )
        return {"recommendations": result.to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}
