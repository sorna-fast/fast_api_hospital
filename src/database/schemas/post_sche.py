from pydantic import BaseModel
from datetime import datetime
from database.schemas import Patient_schemas

class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    creator_id:int
    
    
class PostDisplay(BaseModel):
    id:int
    image_url:str
    image_url_type:str
    caption:str
    timestamp:datetime=datetime.now()
    patient:Patient_schemas.Patient_post
    
    class Config:
        from_attributes = True