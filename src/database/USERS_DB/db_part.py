from database import models
from sqlalchemy.orm import Session
from database.schemas import part_schemas

async def creat_part(db:Session,request:part_schemas.hospital_part):
    try:
        part= models.hospital_part(id=request.id,
                                               part=request.part
                                               )
    except Exception as ex:
        return ex
    
    else:
        db.add(part)
        db.commit()
        db.refresh(part)
        return part
    

async def get_all_part(db:Session):
         user=db.query(models.hospital_part).all()

         return user if user else []

async def get_part(id,db:Session):
    try:
        user=db.query(models.hospital_part).filter(models.hospital_part.id==id).first()
    except Exception as ex:
         return ex
    else: 
        return user
    

async def delete_part(id,db:Session):
    try:
        user = get_part(id,db) 
     
    except Exception as ex:
         return ex
    else:
        db.delete(user)
        db.commit()
        return f"ok {id}"
    

async def update_part(id,db:Session,request:part_schemas.hospital_part):
    try:
        user=db.query(models.hospital_part).filter(models.hospital_part.id==id)
        
    
       
    except Exception as ex:
         return ex
    else:
             user.update({
            id:request.id,
            models.hospital_part.id:request.id,
            models.hospital_part.part:request.part})
