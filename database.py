from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('postgresql://user:password@database:5432/example')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    full_name = Column(String)
    chat_id = Column(String)
    date = Column(Date)
    last_post_id = Column(Integer)

    def __init__(self, username, full_name, date, chat_id, last_post_id=0):
        self.username = username
        self.full_name = full_name
        self.date = date
        self.chat_id = chat_id
        self.last_post_id = last_post_id
