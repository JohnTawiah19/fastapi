from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..models import User
from ..schemas import User as UserSchema, ShowUser as ShowUserSchema
from ..db import get_db
from ..actions import user

router = APIRouter(tags=['users'])


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=ShowUserSchema)
def create_user(request: UserSchema, db: Session = Depends(get_db)):
   return user.create(db, request)
   

@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=ShowUserSchema)
def get_user(id, db: Session = Depends(get_db)):
   return user.get_one(db, id)