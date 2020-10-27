#!env python3
# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# クラス定義
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    kana = Column(String)
    note = Column(String)

dbname = 'tmp.db'
if os.path.exists(dbname):
    os.remove(dbname)

engine = create_engine('sqlite:///' + dbname)
# create table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User()
user.id = 2
user.kana = 'ヤマダタロウ'
user.name = '山田太郎'
user.note = '備考'
session.add(user)
session.commit()

# SELECT * FROM user が内部で実行される
for user in session.query(User).all():
    print(user.name, user.kana)

if os.path.exists(dbname):
    os.remove(dbname)
