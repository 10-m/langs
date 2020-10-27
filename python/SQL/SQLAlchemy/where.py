#!env python3
# -*- coding: utf-8 -*-
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

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
        'maker_id':1,
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

# WHERE
# SELECT * FROM items WHERE itemcode='2000A-NV' LIMIT 1
item_1 = session.query(Item).filter_by(itemcode='2000A-NV').first()
print(item_1.itemcode, item_1.name)

# SELECT * FROM items WHERE maker_id=1 AND price=2500 LIMIT 1
item_2 = session.query(Item).filter_by(maker_id=1, price=2500).first()
print(item_2.itemcode, item_2.price, item_2.maker_id)

# 比較
# SELECT * FROM items WHERE price < 500 LIMIT 1
item_3 = session.query(Item).filter(Item.price < 500).first()
print(item_3.itemcode, item_3.price)

# IN
items_1 = session.query(Item).filter(Item.price.in_([660, 670])).all()
for v in items_1:
    print(v.itemcode, v.price)

items_2 = session.query(Item).filter(
    Item.price.between(1000, 2000)).order_by(Item.price.asc(),
                                             Item.itemcode.asc()).limit(5).all()
for v in items_2:
    print(v.itemcode, v.price)

if os.path.exists(dbname):
    os.remove(dbname)
