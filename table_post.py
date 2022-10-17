from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String 

class Post(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key = True)
	text = Column(String)
	topic = Column(String)

if __name__ == "__main__":
	session = SessionLocal()
	results = session.query(Post).filter(Post.topic == 'business').order_by(Post.id.desc()).limit(10).all()
	print([i.id for i in results])