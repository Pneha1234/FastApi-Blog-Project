from fastapi import FastAPI

from blog import models
from blog.database import engine
from blog.schemas import Blog

app = FastAPI()
models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: Blog):
    return request
    return 'creating blogs'