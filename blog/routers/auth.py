from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Login
from ..db import get_db
from ..models import User
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..token import create_access_token
from datetime import timedelta

router = APIRouter(
    tags=['Authentication']
)

hasher = Hash()

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: User = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
    if not hasher.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid pass')

    #Generate an access token if all credentials are correct
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub":user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}