from database import models
from sqlalchemy.orm import Session
from database.schemas import dr_schemas
from database import hash
async def create_dr(db:Session,request:dr_schemas.DR):
    try:
        user=models.Dr(id=request.id,
                                      name=request.name,
                                      family=request.family,
                                      password=hash.Hash.bcrypt(request.password),
                                      part_id=request.part_id,
                                      
                                      )
    except Exception as ex:
         return ex

    else:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    

async def get_all_dr(db:Session):
         user=db.query(models.Dr).all()

         return user if user else []


async def get_dr(id,db:Session):
    try:
        user=db.query(models.Dr).filter(models.Dr.id==id).first()
    except Exception as ex:
         return ex
    else: 
        return user
    
async def delete_user(id,db:Session):
    try:
        user = get_dr(id,db) 
     
    except Exception as ex:
         return ex
    else:
        db.delete(user)
        db.commit()
        return f"ok {id}"
    
async def update_user(id,db:Session,request:dr_schemas.DR):
    try:
        user=db.query(models.Dr).filter(models.Dr.id==id)
        dr=models.Dr
    
       
    except Exception as ex:
         return ex
    else:
             user.update({
            id:request.id,
            dr.name:request.name,
            dr.family:request.family,
            dr.part_id:request.part_id
            })  