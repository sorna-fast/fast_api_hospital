from fastapi import APIRouter,Depends
from database.db import get_db
from database.USERS_DB import db_Employee
from database.schemas.Employee_schemas import Employee,Employee_dispalay
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_scheme

router=APIRouter(prefix="/Employee",tags=["Employee"])


@router.post("/create_user_Employee/")
async def create_users_Employee(request:Employee,db:Session=Depends(get_db)):
    return await db_Employee.creat_user(db=db,request=request)


@router.get("/get_all_Employee/",response_model=list[Employee_dispalay])
async def get_all_Employee(db:Session=Depends(get_db)):
   return await db_Employee.get_all_user(db=db)


@router.get("/get_one_Employee/{id}",response_model=Employee_dispalay)
async def get_one_Employee(id:int,db:Session=Depends(get_db)):
    return await db_Employee.get_user(id=id,db=db)


@router.put("/update_Employee/{id}")
async def update_user_Employee(id:int,user:Employee,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Employee.update_Nurse(id=id,db=db,requset=user)


@router.delete("/delete_Employee/{id}")
async def delete_user_Employee(id:int,db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    return await db_Employee.delete_user(id=id,db=db)
