from pydantic import BaseModel
from fastapi import Path,Query
from typing import List
from database.schemas.Patient_schemas import Patient_Dispalay

class Dr_base(BaseModel):
    id:int
    name:str
    family:str

class DR(Dr_base):
    password:str = Path(title="password DR", min_length=4,max_length=16)
    part_id:int
    

class DR_dispalay(Dr_base):
    part_id:int
    patient:List[Patient_Dispalay]
    class Config:
        from_attributes = True
        

class DR_showpart(Dr_base):
    class Config:
        from_attributes = True    

class DR_post(BaseModel):
    id:str
    name:str
    class Config:
        from_attributes = True  