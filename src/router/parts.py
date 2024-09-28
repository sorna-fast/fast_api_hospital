from fastapi import APIRouter,Depends
from database.db import get_db
from database.USERS_DB import db_part
from database.schemas.part_schemas import hospital_part,haspital_part_show
from sqlalchemy.orm import Session
router=APIRouter(prefix="/part",tags=["part"])





@router.post("/create_user_part/")
async def create_users_part(request:hospital_part,db:Session=Depends(get_db)):
    return await db_part.creat_part(db=db,request=request)


@router.get("/get_all_part/",response_model=list[hospital_part])
async def get_all_part(db:Session=Depends(get_db)):
   return await db_part.get_all_part(db=db)


@router.get("/get_part/{id}",response_model=haspital_part_show)
async def get_one_part(id:int,db:Session=Depends(get_db)):
    return await db_part.get_part(id=id,db=db)


@router.put("/update_part/{id}")
async def update_user_part(id:int,user:hospital_part,db:Session=Depends(get_db)):
    return await db_part.update_part(id=id,db=db,requset=user)


@router.delete("/delete_part/{id}")
async def delete_user_part(id:int,db:Session=Depends(get_db)):
    return await db_part.delete_part(id=id,db=db)
