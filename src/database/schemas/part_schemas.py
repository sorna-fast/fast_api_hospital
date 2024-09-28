from pydantic import BaseModel
from fastapi import Path
from typing import List
from database.schemas import dr_schemas,Employee_schemas,Nurse_schemas

class hospital_part(BaseModel):
    id:int
    part:str=Path(min_length=4,max_length=16)
    class Config:
        from_attributes = True


class haspital_part_show(BaseModel):
    id:int
    part:str
    dr:list[dr_schemas.DR_showpart]
    employee:list[Employee_schemas.Employee_showpart]
    nurses:list[Nurse_schemas.Nurse_show_part]
    class Config:
        from_attributes = True
        
        
        