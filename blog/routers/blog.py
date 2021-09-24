from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..schemas import ShowBlog as ShowBlogSchema, Blog as BlogSchema, User as UserSchema
from ..db import get_db
from ..models import Blog
from typing import List
from ..actions import blog as BlogActions
from ..oauth2 import get_current_user

router = APIRouter(
    tags=['blogs']
)

@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create(req: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
   return BlogActions.create(db, req)
    
@router.get('/blog', response_model=List[ShowBlogSchema])
def blogs(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return BlogActions.get_all(db)

@router.get('/blog/{id}', response_model=ShowBlogSchema)
def blog(id, response: Response, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return BlogActions.get_one(db, id)

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
   return BlogActions.update(db, id, request) 
     
@router.delete('/blog/{id}', status_code= status.HTTP_200_OK)
def destroy(id, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return BlogActions.destroy(db, id)