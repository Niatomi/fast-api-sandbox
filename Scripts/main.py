import uvicorn

from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi import status

from exceptions import PostNotFoundException

from database import Database

from schemas import Post

app = FastAPI()

db = Database()

@app.exception_handler(PostNotFoundException)
def handle_post_not_found_exception(request: Request, exc: PostNotFoundException):
    return Response(
        content="Post not found",
        status_code=status.HTTP_404_NOT_FOUND
    )

@app.post('/create')
def creae_post(post: Post):
    return db.create_post(post)

@app.get('/posts')
def get_posts():
    return db.get_all()

@app.get('/posts/{id}')
def get_posts(id: int):
    return db.get_by_id(id)

@app.patch('/posts/{id}')
def update_post(id: int, post: Post):
    return db.update_by_id(id, post)

@app.delete('/posts/{id}')
def delete_post(id: int):
    return db.delete_by_id(id)

def main():
    uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True)

if __name__ == "__main__":
    main()