#!env python3
# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    kana = Column(String(45), nullable=False)
    note = Column(String(100))

dbname = 'tmp.db'
if os.path.exists(dbname):
    os.remove(dbname)

engine = create_engine('sqlite:///' + dbname)
# create table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User()
user1.id = 1
user1.kana = 'タナカイチロウ'
user1.name = '田中一郎'
user1.note = '備考'
session.add(user1)

user2 = User()
user2.id = 2
user2.kana = 'ヤマダタロウ'
user2.name = '山田太郎'
user2.note = '備考'
session.add(user2)
session.commit()

# トランザクション制御
try:
    user1 = session.query(User).get(1)
    user2 = session.query(User).get(2)
    user1.name = 'あいうえお'
    user2.name = 'かきくけこ'
    session.add(user1)
    session.add(user2)
    raise ValueError('Roll back')
    session.commit()

except:  # noqa: E722
    print('start rollback')
    session.rollback()

finally:
    session.close()

user1 = session.query(User).get(1)
print(user1.name)
user2 = session.query(User).get(2)
print(user2.name)

if os.path.exists(dbname):
    os.remove(dbname)
