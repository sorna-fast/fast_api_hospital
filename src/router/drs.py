from fastapi import APIRouter,Depends
from database.db import get_db
from database.USERS_DB import db_dr
from database.schemas.dr_schemas import DR,DR_dispalay
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_scheme
router=APIRouter(prefix="/Dr",tags=["Dr"])


@router.post("/create_user_Dr/",response_model=DR_dispalay)
async def create_users_dr(request:DR,db:Session=Depends(get_db)):
    return await db_dr.create_dr(db=db,request=request)


@router.get("/get_all_Dr/",response_model=list[DR_dispalay])
async def get_all_Dr(db:Session=Depends(get_db)):
   return await db_dr.get_all_dr(db=db)


@router.get("/get_one_Dr/{id}",response_model=DR_dispalay)
async def get_one_Dr(id:int,db:Session=Depends(get_db)):
    return await db_dr.get_dr(id=id,db=db)


@router.put("/update_user_Dr/{id}")
async def update_user_Dr(id:int,user:DR,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_dr.update_user(id=id,db=db,requset=user)


@router.delete("/delete_user_Dr/{id}")
async def delete_user_Dr(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_dr.delete_user(id=id,db=db)
