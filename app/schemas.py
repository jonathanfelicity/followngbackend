from pydantic import BaseModel



class UserModel(BaseModel):
    username: str
    instagram_id: str





class CampaignModel(BaseModel):
    type: str
    engagement: int
    owner: int