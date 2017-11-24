#!env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

nobel_winners = [{
    'category': 'physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921
}, {
    'category': 'physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1933
}, {
    'category': 'chemistry',
    'name': 'Marle Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1911
}]

engine = create_engine('sqlite:///nobel_prize.db', echo=True)
Base = declarative_base()

class Winner(Base):
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"\
            %(self.name, self.category, self.year)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

albert = Winner(**nobel_winners[0])
session.add(albert)
print(session.new)

session.expunge(albert)
print(session.new)

winner_rows = [Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
print(session.commit())

print(session.query(Winner).count())

result = session.query(Winner).filter_by(nationality='Swiss')   # ?
print(list(result))

result = session.query(Winner).filter(\
             Winner.category == 'physics', \
             Winner.nationality != 'Swiss')
print(list(result))


print(session.query(Winner).get(3))

res = session.query(Winner).order_by('year')
print(list(res))

marie = session.query(Winner).get(3)
marie.nationality = 'French'
print(session.dirty)
print(session.commit())

session.query(Winner).filter_by(name='Albert Einstein').delete()
print(list(session.query(Winner)))
