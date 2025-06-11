from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_id: str

