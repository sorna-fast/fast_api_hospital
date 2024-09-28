from pydantic import BaseModel
from fastapi import Path
from typing import List
from database.schemas.Patient_schemas import Patient_Dispalay

class Employee_base(BaseModel):
    id:int
    name:str
    family:str
    


class Employee(Employee_base):
    part_id:int
    password:str = Path(title="password Employee", min_length=4,max_length=16)



class Employee_dispalay(Employee_base):
    part_id:int
    patient:list[Patient_Dispalay]
    class Config:
        from_attributes = True
    
class Employee_showpart(Employee_base):
    id:int
    name:str
    family:str
    class Config:
        from_attributes = True
        