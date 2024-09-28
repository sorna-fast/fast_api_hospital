from fastapi import APIRouter,Depends
from database.db import get_db
from database.USERS_DB import db_Nurse
from database.schemas.Nurse_schemas import Nurse,Nurse_dispalay
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_scheme


router=APIRouter(prefix="/Nurse",tags=["Nurse"])


@router.post("/create_user_Nurse/",response_model=Nurse_dispalay)
async def create_users_Nurse(request:Nurse,db:Session=Depends(get_db)):
    return await db_Nurse.creat_user(db=db,request=request)


@router.get("/get_all_Nurse/",response_model=list[Nurse_dispalay])
async def get_all_Nurse(db:Session=Depends(get_db)):
   return await db_Nurse.get_all_user(db=db)


@router.get("/get_Nurse/{id}",response_model=Nurse_dispalay)
async def get_one_Nurse(id:int,db:Session=Depends(get_db)):
    return await db_Nurse.get_user(id=id,db=db)


@router.put("/update_Nurse/{id}")
async def update_user_Nurse(id:int,user:Nurse,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Nurse.update_Nurse(id=id,db=db,requset=user)


@router.delete("/delete_Nurse/{id}")
async def delete_user_Nurse(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Nurse.delete_user(id=id,db=db)
