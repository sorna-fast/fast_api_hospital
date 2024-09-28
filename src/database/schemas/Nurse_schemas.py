from pydantic import BaseModel
from fastapi import Path
from typing import List
from database.schemas.Patient_schemas import Patient_Dispalay

class base_Nurse(BaseModel):
    id:int
    name:str
    family:str
    

class Nurse(base_Nurse):
    password:str = Path(title="password Nurse", min_length=4,max_length=16)
    part_id:int
    


class Nurse_dispalay(base_Nurse):
    part_id:int
    patient:list[Patient_Dispalay]
    class Config:
        from_attributes = True

class Nurse_show_part(base_Nurse):
    class Config:
        from_attributes = True