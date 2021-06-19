from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs list from the database'}
    else:
        return {'data': f'{limit} blogs list from the database'}


@app.get('/blog/unpublished')
def unpublished_blog():
    # fetch all unpublished blog
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show_blog(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id =id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title:str
    body:str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return{'data': f"Blog is created with request as{request}"}
