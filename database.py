from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml" #ссылочка на на базу данных 

engine = create_engine(SQLALCHEMY_DATABASE_URL) #двигатель, который устраняет все различия между базами данных и их языками 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #фабрика сессий, в которой можно прописать параметры для сессий,
																			#не указывая их каждый раз вручную  
Base = declarative_base() #класс для написания представлений таблиц, от которого нужно наследоваться 