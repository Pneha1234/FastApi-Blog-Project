from typing import Optional

from fastapi import FastAPI

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
