from database import models
from sqlalchemy.orm import Session
from database import hash
from database.schemas import Patient_schemas
from datetime import datetime




async def creat_user(db: Session, request: Patient_schemas.Patient_Base):
    try:
        print("Request data:", request)
        user = models.Patient(
            id=request.id,
            name_Patient=request.name_Patient,
            family_Patient=request.family_Patient,
            password=hash.Hash.bcrypt(request.password),
            parts_Patient=request.parts_Patient,
            datatime=request.datatime,
            dr_id=request.dr_id_Patient,
            employee_id=request.employee_id,
            Nurse_id=request.nurse_id,
            National_Code=request.National_Code
        )
        print("User to add:", user)
    except Exception as ex:
        print("Error in creating user:", ex)
        return ex
    
    db.add(user)
    db.commit()
    db.refresh(user)
    print("User added:", user)
    return user



    
    

async def get_all_user(db:Session):
         user=db.query(models.Patient).all()

         return user if user else []

async def get_user(id,db:Session):
    try:
        user=db.query(models.Patient).filter(models.Patient.id==id).first()
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
    

async def update_Patient(id,db:Session,request:Patient_schemas.Patient_Base):
    try:
        user=db.query(models.Patient).filter(models.Patient.id==id)
        
    
       
    except Exception as ex:
         return ex
    else:
             user.update({
            id:request.id,
            models.Patient.id:request.id,
            models.Patient.name_Patient:request.name_Patient,
            models.Patient.family_Patient:request.family_Patient,
            models.Patient.part:request.parts_Patient,
            models.Patient.datatime:request.datatime,
            models.Patient.dr_id:request.dr_id_Patient,
            models.Patient.employee_id:request.employee_id,
            models.Patient.Nurse_id:request.nurse_id,
            models.Patient.National_Code:request.National_Code})
    return "Ok"
