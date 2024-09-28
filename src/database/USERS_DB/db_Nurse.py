from database import models
from sqlalchemy.orm import Session
from database.schemas import Nurse_schemas
from database import hash


async def creat_user(db:Session,request:Nurse_schemas.Nurse):
    try:
        user= models.Nurse(id=request.id,
                                    name=request.name,
                                    family=request.family,
                                    password=hash.Hash.bcrypt(request.password),
                                    part_id=request.part_id
                                               )
    except Exception as ex:
        return ex


    else:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    

async def get_all_user(db:Session):
         user=db.query(models.Nurse).all()

         return user if user else []

async def get_user(id,db:Session):
    try:
        user=db.query(models.Nurse).filter(models.Nurse.id==id).first()
    except Exception as ex:
         return ex
    else: 
        return user
    

async def delete_user(id,db:Session):
    try:
        user = get_user(id,db) 
     
    except Exception as ex:
         return ex
    else:
        db.delete(user)
        db.commit()
        return f"ok {id}"
    

async def update_Nurse(id,db:Session,request:Nurse_schemas.Nurse):
    try:
        user=db.query(models.Nurse).filter(models.Nurse.id==id)
        
    
       
    except Exception as ex:
         return ex
    else:
             user.update({
            id:request.id,
            models.Nurse.id:request.id,
            models.Nurse.part:request.name,
            models.Nurse.family:request.family,
            models.Nurse.part_id:request.part_id})
