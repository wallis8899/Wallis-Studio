import streamlit as st
from PIL import Image
from sqlalchemy import create_engine,String,ForeignKey,Integer,Column
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()
class Video(Base):
	__tablename__ = "Video"
	postId = Column("Id",String,primary_key=True,default=str(uuid.uuid4()))
	Url = Column("Url",String)
	Title = Column("Title",String)
	Desc = Column("Desc",String)
	"""docstring for ClassName"""
	def __init__(self, Url,Title,Desc):
		self.Url = Url
		self.Title = Title
		self.Desc = Desc
		


db = "sqlite:///database//Wallisdb.db"
engine = create_engine(db)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
session = Session()



