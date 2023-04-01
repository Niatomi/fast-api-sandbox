import uvicorn

from fastapi import FastAPI
from schema import Post

app = FastAPI(
    title='Full fast-api course',
    contact='playervoker@gmail.com'
)

fake_posts_db = []

@app.get("/")
def get_basic_page():
    return 'Server is runninng'

@app.post
def save_post(post: Post):
    print(post.title)
    fake_posts_db.append(post)
    return f'Saved post with title {post.title}...'

@app.get('/get_all_the_posts')
def get_all_the_posts():
    return fake_posts_db


def main():
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=4201)
    

if __name__ == "__main__":
    main()