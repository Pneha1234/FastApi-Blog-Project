from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str

@app.post('/blog')
def create(request:Blog):
    return request
    return 'creating blogs'