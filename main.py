from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data': {'name': 'John'}}

@app.get('/about')
def about():
    return 'contact us'