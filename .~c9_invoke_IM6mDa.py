from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
Base.metadata.create_all(engine)

radio = Item(name="CS1008", description="Radio from 1998")
session.add(radio)

shoes = Item()
shoes.name = "sneakers"
session.add(shoes)

session.commit()

items = session.query(Item).all()
print(items)

for item in items:
    print(item.name)
    
sneakers = session.query(Item).filter(Item.name == 'sneakers').all()
print(sneakers)


user = session.delete(User).