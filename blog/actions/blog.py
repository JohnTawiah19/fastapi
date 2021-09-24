from ..models import Blog
from ..schemas import Blog as BlogSchema
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def get_one(db: Session, id:int):
    blog: Blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog does not exist")
    return blog

def create(db: Session, request: BlogSchema):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(db: Session, id:int, request:BlogSchema):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with title {request.title} not found')
    blog.update(request.dict())
    db.commit()
    return 'blogpost has been updated'

def destroy(db: Session, id:int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog does not exist')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog deleted'
