import random
import shutil
from fastapi import APIRouter,Depends,status,UploadFile,File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database.db import get_db 
from database.USERS_DB import db_post
from database.schemas.post_sche import PostBase,PostDisplay
from database.schemas.dr_schemas import DR_post

from typing import List
from string import ascii_letters
from auth import oauth2

router=APIRouter(prefix="/post",tags=["post"])

image_url_tyopes=["url","uploaded"]

@router.post("/create_post",response_model=PostDisplay)
def create_post(request:PostBase,db:Session=Depends(get_db),
                current_user:DR_post=Depends(oauth2.get_current_user)):
    if request.image_url_type not in image_url_tyopes:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="image url type should be 'uploded' or 'uploaded' ")

    return db_post.create_post(request,db)



@router.get("/",response_model=List[PostDisplay])
def get_post(db:Session=Depends(get_db)):
    postes=db_post.get_all_post(db)
    return postes if postes else []

@router.post("/upload_file")
def upload_file(file:UploadFile=File(...)):

    rand_star = "".join(random.choice(ascii_letters)for _ in range(6))
    new_name=f"_{rand_star}".join(file.filename.rsplit(".",1))
    path_file=f"uploaded_file/{new_name}"

    with open(path_file,"w+b") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {"path_file":path_file}