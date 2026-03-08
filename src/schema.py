from pydantic import BaseModel

class CreatePost(BaseModel): 
    user: str
    title: str
    content: str

class PostResponse(BaseModel): 
    user: str
    title: str
    content: str