from fastapi import FastAPI
from .models import Base
from .db import engine
from .routers import blog, user, auth

#Database server
Base.metadata.create_all(engine)

#Api routes
app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)



    
