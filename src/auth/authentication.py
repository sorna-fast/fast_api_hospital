from fastapi import APIRouter,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from database import models
from database.db import get_db
from sqlalchemy.orm import Session
from database.hash import Hash
from auth import oauth2


router=APIRouter(tags=["authentication"])



@router.post("/token")
def get_token(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.Dr).filter(models.Dr.name==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credential")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credential")

    access_token =oauth2.create_access_token(data={"sub":request.username})

    return {
        "access_token":access_token,
        "type_token":"bearer",
        "userID":user.id,
        "useername":user.name
    }

