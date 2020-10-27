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

# insert
user = User()
user.id = 5
user.kana = 'タナカイチロウ'
user.name = '田中一郎'
user.note = '備考'
session.add(user)
session.commit()

add_user = session.query(User).order_by(User.id.desc()).first()
print(add_user.kana, add_user.name, add_user.note)

# update
update_user = session.query(User).filter(User.id == 5).first()
update_user.kana = 'アップデート'
update_user.name = 'テスト更新'
session.add(update_user)
session.commit()
user = session.query(User).filter(User.id == 5).first()
print(user.name, user.kana)

# delete
# ユーザーテーブルのレコードを削除
session.query(User).filter(User.name == 'アップデート').delete()
session.commit()
user = session.query(User).filter(User.name == 'アップデート').first()
print(user)

if os.path.exists(dbname):
    os.remove(dbname)
