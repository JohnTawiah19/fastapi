from ..hashing import Hash
from ..models import User
from ..schemas import User as UserSchema
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


hasher = Hash()

def create(db:Session , request: UserSchema):
    new_user = User(name=request.name, email=request.email, password=hasher.hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User does not exist')
    return user