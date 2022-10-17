from fastapi import FastAPI, Depends
from table_user import User
from table_post import Post
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet
from fastapi import HTTPException
from typing import List
from database import SessionLocal
from typing import List
from sqlalchemy import func

app = FastAPI()

# def get_db():

def sessionmaker():
	session = SessionLocal()
	return session

@app.get("/user/{id}", response_model = UserGet)
def getuser(id:int, session = Depends(sessionmaker)):
	results = session.query(User).filter(User.id == id).one_or_none()
	if results == None:
		raise HTTPException(status_code=404)
	return results

@app.get("/post/{id}", response_model = PostGet)
def getpost(id:int, session = Depends(sessionmaker)):
	results = session.query(Post).filter(Post.id == id).one_or_none()
	if results == None:
		raise HTTPException(status_code=404)
	return results

@app.get("/user/{id}/feed", response_model = List[FeedGet])
def getuserfeed(id:int, limit:int = 10, session = Depends(sessionmaker)):
	results = session.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
	return results

@app.get("/post/{id}/feed", response_model = List[FeedGet])
def getpostfeed(id:int, limit: int = 10, session = Depends(sessionmaker)):
	results = session.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
	return results

@app.get("/post/recommendations/", response_model = List[PostGet])
def getfavepost(id:int = 205, limit: int = 10, session = Depends(sessionmaker)):
	results = session.query(Post.id, Post.text, Post.topic).join(Feed).filter(Feed.action == 'like')\
	.group_by(Post.id).order_by(func.count(Post.id).desc()).limit(limit).all()
	return results 