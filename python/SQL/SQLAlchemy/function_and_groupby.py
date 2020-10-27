#!env python3
# -*- coding: utf-8 -*-
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, func

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    itemcode = Column(String, unique=True)
    name = Column(String)
    price = Column(Integer)
    cost_price = Column(Integer)
    maker_id = Column(Integer)

dbname = 'tmp.db'
if os.path.exists(dbname):
    os.remove(dbname)

engine = create_engine('sqlite:///' + dbname)
# create table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

records = [
    {
        'id':1,
        'itemcode':'2000A-NV',
        'name':'hoge',
        'price':2500,
        'cost_price':100,
        'itemname':'hoge',
        'maker_id':1,
    },
    {
        'id':2,
        'itemcode':'ABC',
        'name':'hoge',
        'price':200,
        'cost_price':100,
        'itemname':'hoge',
        'maker_id':1,
    },
    {
        'id':3,
        'itemcode':'def',
        'name':'hoge',
        'price':660,
        'cost_price':100,
        'itemname':'hoge',
        'maker_id':1,
    },
    {
        'id':4,
        'itemcode':'ghi',
        'name':'hoge',
        'price':1100,
        'cost_price':100,
        'itemname':'hoge',
        'maker_id':2,
    }
]

for record in records:
    item = Item()
    item.id = record['id']
    item.itemcode = record['itemcode']
    item.name = record['name']
    item.price = record['price']
    item.cost_price = record['cost_price']
    item.maker_id = record['maker_id']
    session.add(item)
session.commit()

# SELECT count(id) FROM items
# scalar関数は、取得した結果の最初の要素かNoneを返す
cnt = session.query(func.count(Item.id)).scalar()
print(cnt)

# SELECT maker_id, count(id) AS cnt FROM items GROUP BY maker_id
groups = session.query(
    Item.maker_id,
    func.count(Item.id).label('cnt')
).group_by(Item.maker_id).all()

for v in groups:
    print(v.maker_id, v.cnt)

# HAVING
groups = session.query(
    Item.maker_id,
    func.count(Item.id).label('cnt')).group_by(Item.maker_id).having(
        func.count(Item.id) >= 2).all()

for v in groups:
    print(v.maker_id, v.cnt)

# SUM, MIN, MAX
result = session.query(
    func.count(Item.id).label('cnt'),
    func.sum(Item.price).label('p_total'),
    func.max(Item.price).label('p_max'),
    func.min(Item.price).label('p_min')
).filter(Item.maker_id == 1).first()

print(result)

if os.path.exists(dbname):
    os.remove(dbname)
