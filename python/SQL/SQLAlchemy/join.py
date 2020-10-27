#!env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# sample data
session.add(User(id=1, name="Suzuki", age=19))
session.add(User(id=2, name="Tanaka", age=21))
session.add(User(id=3, name="Sato", age=21))

session.add(Post(users_id=1, title="gym"))
session.add(Post(users_id=1, title="dinner"))
session.add(Post(users_id=2, title="work"))
session.add(Post(users_id=2, title="python"))
session.commit()

print('--- inner join')
users_posts = session.query(User, Post).join(Post, User.id == Post.users_id).all()

for user_posts in users_posts:
    print(user_posts.User.name, user_posts.Post.title,)

print('--- left outer join')
users_posts = session.query(User, Post).outerjoin(Post, User.id == Post.users_id).all()

for user_posts in users_posts:
    if user_posts.Post is not None:
        print(user_posts.User.name, user_posts.Post.title,)
    else:
        print(user_posts.User.name)
