from fastapi import FastAPI
from pydantic import BaseModel  # FastAPI import

app = FastAPI()


@app.get("/")
def printHello():
    return "Hello World"


@app.get("/json")
def printJson():
    return {"Number": 12345}


class Post(BaseModel):
    title: str
    content: str


@app.post("/posts")
def createContents(post: Post):
    title = post.title
    content = post.content

    return {"item": post}
