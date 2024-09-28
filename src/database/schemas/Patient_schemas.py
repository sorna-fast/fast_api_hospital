from pydantic import BaseModel
from fastapi import Path
from typing import List
from datetime import datetime

class Patient_Base(BaseModel):
    id:int
    name_Patient:str
    family_Patient:str
    password:str = Path(title="password Patient", min_length=4,max_length=16)
    parts_Patient:int
    datatime:datetime
    dr_id_Patient:int
    employee_id:int
    nurse_id:int
    National_Code:int
    class Config:
        from_attributes = True
    


class Patient_Dispalay(BaseModel):
    id:int
    name_Patient:str
    family_Patient:str
    parts_Patient:int

    class Config:
        from_attributes = True
        
class Patient_post(BaseModel):
    id:int
    class Config:
        from_attributes = True