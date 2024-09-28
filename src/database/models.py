from database.db import base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship





 
 
class SubClass:
    id=Column("id",Integer,unique=True,primary_key=True,index=True)
        
class hospital_part(SubClass,base):
    __tablename__="Hospital_Part"
    part=Column("part",String(50),unique=True,primary_key=True)
        
    dr=relationship("Dr",back_populates="part")
    employee=relationship("Employee",back_populates="part")
    nurses=relationship("Nurse",back_populates="part")
    patients=relationship("Patient",back_populates="part")

class Dr(SubClass,base):
    __tablename__="dr"
    name=Column("name",String(50))
    family=Column("family",String(50))
    password=Column("password",String(200))
    part_id=Column("part",Integer,ForeignKey("Hospital_Part.id"))
    part=relationship("hospital_part",back_populates="dr")
        
        

    patient=relationship("Patient",back_populates="visit_dr")

class Employee(SubClass,base):
    __tablename__="employee"
    name=Column("name",String(50))
    family=Column("family",String(50))
    password=Column("password",String(200))

    part_id=Column("part",Integer,ForeignKey("Hospital_Part.id"))
    part=relationship("hospital_part",back_populates="employee")

        
    patient=relationship("Patient",back_populates="visit_employee")


class Nurse(SubClass,base):
    __tablename__="nurse"
    name=Column("name",String(50))
    
    family=Column("family",String(50))
    password=Column("password",String(200))

    part_id=Column("part_id",Integer,ForeignKey("Hospital_Part.id"))
    part=relationship("hospital_part",back_populates="nurses")
        
    patient=relationship("Patient",back_populates="visit_Nurse")

class Patient(SubClass,base):
    __tablename__="patient"
    name_Patient=Column("name",String(50))
    family_Patient=Column("family",String(50))
    password=Column("password",String(200))
    
    parts_Patient=Column("part_id",Integer,ForeignKey("Hospital_Part.id"))

    part=relationship("hospital_part",back_populates="patients")
    datatime=Column("DateTime",DateTime)
    dr_id=Column("dr",Integer,ForeignKey("dr.id"))
    visit_dr=relationship("Dr",back_populates="patient")
    

    employee_id=Column("employee",Integer,ForeignKey("employee.id"))
    visit_employee=relationship("Employee",back_populates="patient")

    Nurse_id=Column("Nurse",Integer,ForeignKey("nurse.id"))
    visit_Nurse=relationship("Nurse",back_populates="patient")
        
    National_Code=Column("National_Code",Integer,unique=True)
    posts=relationship("Post",back_populates="patient")

class Post(base):
    __tablename__="post"

    id=Column("id",Integer,index=True,primary_key=True)
    image_url=Column("image_url",String(100))
    image_url_type=Column("image_url_type",String(100))
    caption= Column("caption",String(100))
    timestamp=Column("timestamp",DateTime)
    patient_id=Column("patient_id",Integer,ForeignKey("patient.id"))
    patient=relationship("Patient",back_populates="posts")