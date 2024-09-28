from database import models
from sqlalchemy.orm import Session
from database import hash
from database.schemas import Employee_schemas



async def creat_user(db:Session,request:Employee_schemas.Employee):
    try:
        user= models.Employee(id=request.id,
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
         user=db.query(models.Employee).all()

         return user if user else []

async def get_user(id,db:Session):
    try:
        user=db.query(models.Employee).filter(models.Employee.id==id).first()
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
    

async def update_Nurse(id,db:Session,request:Employee_schemas.Employee):
    try:
        user=db.query(models.Employee).filter(models.Employee.id==id)
        
    
       
    except Exception as ex:
         return ex
    else:
             user.update({
            id:request.id,
            models.Employee.id:request.id,
            models.Employee.part:request.name,
            models.Employee.family:request.family,
            models.Employee.part_id:request.part_id})
