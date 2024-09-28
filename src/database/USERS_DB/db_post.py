from database.models import Post 
from database.schemas.post_sche import PostBase
from sqlalchemy.orm import Session
from datetime import datetime

def create_post(request:PostBase,db:Session):
    new_post=Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_post(db:Session):
    Postes=[]
    for x in db.query(Post).all():
        Postes.append(x)
    return Postes

    