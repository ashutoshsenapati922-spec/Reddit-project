from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, User, Community, Post, Comment
from auth import hash_password

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Reddit Clone API"}

# Register User
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = User(
        username=username,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()

    return {"message": "User created"}

# Create Community
@app.post("/community")
def create_community(name: str, description: str,
                     db: Session = Depends(get_db)):

    community = Community(
        name=name,
        description=description
    )

    db.add(community)
    db.commit()

    return {"message": "Community created"}

# Get Communities
@app.get("/communities")
def get_communities(db: Session = Depends(get_db)):
    return db.query(Community).all()

# Create Post
@app.post("/post")
def create_post(title: str, content: str,
                db: Session = Depends(get_db)):

    post = Post(
        title=title,
        content=content
    )

    db.add(post)
    db.commit()

    return {"message": "Post created"}

# Get Posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

# Vote
@app.post("/vote/{post_id}")
def vote(post_id: int, vote_type: int,
         db: Session = Depends(get_db)):

    post = db.query(Post).filter(Post.id == post_id).first()

    post.votes += vote_type

    db.commit()

    return {"votes": post.votes}

# Add Comment
@app.post("/comment")
def add_comment(post_id: int, text: str,
                db: Session = Depends(get_db)):

    comment = Comment(
        post_id=post_id,
        text=text
    )

    db.add(comment)
    db.commit()

    return {"message": "Comment added"}

# Get Comments
@app.get("/comments/{post_id}")
def get_comments(post_id: int,
                 db: Session = Depends(get_db)):

    return db.query(Comment).filter(
        Comment.post_id == post_id
    ).all()