from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

#Get Requests
@app.get('/')
def index():
    return {'data': 'blog list'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'show unpublished blogs'}

@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

#Post Requests
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return f'Blog ia created with title as {blog.title}'

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= 5000)