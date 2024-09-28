from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime,timedelta
from jose import jwt
from fastapi import Depends,status
from sqlalchemy.orm import Session
from database.db import get_db
from fastapi.exceptions import HTTPException
from jose.exceptions import JWTError
oauth2_scheme =OAuth2PasswordBearer(tokenUrl="token")



SECRET_KEY ="120049407451447e508bbafea25f840b8c7abb40ea32758d3442d37034f0cb25"
ALGORITHM = "HS256"
#=======================
#مقدار زمان مصرف توکن 
ACCESS_TOKEN_EXPIRE_MINUTES =30


def create_access_token(data:dict,expries_delta:Optional[timedelta]= None):
    to_encode =data.copy()
    if expries_delta:
        expire =datetime.utcnow() + expries_delta
    else:
        expire = datetime.utcnow()+ timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    error_credential=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail="invalid credentials",
                                   headers={"WWW-authenticate":"bearer"})
    

    try:
        _dict=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username=_dict.get("sub")
        if not username:
            raise error_credential

    except JWTError:
        raise error_credential