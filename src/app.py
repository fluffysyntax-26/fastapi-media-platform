from fastapi import FastAPI, HTTPException
from src.schema import Posts, CreatePost, PostResponse

app = FastAPI()

text_posts = {
    1: {
        "user": "Deepak",
        "title": "first post",
        "content": "lorem ipsum dolor sit amet"
    },

    2: {
        "user": "Prateek",
        "title": "sample post",
        "content": "this is my sample post"
    },

    3: {
        "user": "Aisha",
        "title": "learning fastapi",
        "content": "fastapi makes building apis extremely simple and fast"
    },

    4: {
        "user": "Rahul",
        "title": "python tips",
        "content": "list comprehensions can make your python code cleaner and shorter"
    },

    5: {
        "user": "Neha",
        "title": "cloud journey",
        "content": "starting my journey with aws and cloud computing today"
    },

    6: {
        "user": "Arjun",
        "title": "backend development",
        "content": "understanding databases and api design is crucial for backend engineers"
    },

    7: {
        "user": "Sana",
        "title": "machine learning basics",
        "content": "supervised learning requires labeled datasets to train models"
    },

    8: {
        "user": "Karan",
        "title": "docker notes",
        "content": "containers help keep applications consistent across environments"
    },

    9: {
        "user": "Meera",
        "title": "javascript vs python",
        "content": "both languages are powerful but serve different purposes in development"
    },

    10: {
        "user": "Rohan",
        "title": "dev productivity",
        "content": "keyboard shortcuts and good tooling can drastically improve productivity"
    },

    11: {
        "user": "Ishaan",
        "title": "data structures",
        "content": "hash maps provide average constant time complexity for lookups"
    },

    12: {
        "user": "Priya",
        "title": "ai future",
        "content": "artificial intelligence will transform many industries in the coming decade"
    }
}

# the data that you return from an endpoint should always be a pydantic object or a python dictionary
@app.get("/")
def hello_world() -> dict: 
    return {'message':'Hello, World!'} # JSON


@app.get("/posts")
def get_posts(limit: int = None):
    if limit: 
        return list(text_posts.values())[:limit]
    return text_posts 

@app.get('/posts/{id}')
def get_post_by_id(id:int) -> PostResponse:
    if id not in text_posts: 
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts") 
def create_post(post: CreatePost) -> CreatePost:
    new_post = {
        "user": post.user,
        "title": post.title, 
        "content": post.content
    } 

    text_posts[max(text_posts.keys()) + 1] = new_post

    return new_post

