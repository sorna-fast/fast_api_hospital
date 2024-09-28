from fastapi import APIRouter,Depends
from database.db import get_db
from database.USERS_DB import db_Patient
from database.schemas.Patient_schemas import Patient_Base,Patient_Dispalay
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_scheme


router=APIRouter(prefix="/Patient",tags=["Patient"])


@router.post("/create_user_Patient/")
async def create_users_Patient(request:Patient_Base,db:Session=Depends(get_db)):
    print("Received request:", request)
    return await db_Patient.creat_user(db=db,request=request)


@router.get("/get_Patient/",response_model=list[Patient_Dispalay])
async def get_all_Patient(db:Session=Depends(get_db)):
   return await db_Patient.get_all_user(db=db)


@router.get("/get_Patient/{id}")
async def get_one_Patient(id:int,db:Session=Depends(get_db)):
    return await db_Patient.get_user(id=id,db=db)


@router.put("/update_Patient/{id}")
async def update_user_Patient(id:int,user:Patient_Base,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Patient.update_Patient(id=id,db=db,requset=user)


@router.delete("/delete_Patient/{id}")
async def delete_user_Patient(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Patient.delete_user(id=id,db=db)
