from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    items = relationship("Item", backref="user")
    bids = relationship("Bid", backref="user")
    

class Item(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    bids = relationship("Bid", backref="item")


class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    


# USERS 
amanda = User(username="Amanda", password="Apples")

bob = User(username="Bob", password="Blueberries")

candice = User(username="Candice", password="Coconuts")

# ITEMS 
baseball = Item(name="Baseball", user=bob)

session.add_all([amanda, bob, candice, baseball])

# BIDS 
amandabid1 = Bid(price=5.0, user=amanda, item=baseball)
session.add(amandabid1)

amandabid2 = Bid(price=15.0, user=amanda, item=baseball)
session.add(amandabid2)

candicebid1 = Bid(price=10.0, user=candice, item=baseball)
session.add(candicebid1)

candicebid2 = Bid(price=20.0, user=candice, item=baseball)
session.add(candicebid2)


# QUERYING 
bids = session.query(Bid.price).filter(Bid.item_id == 1).order_by(Bid.price).all()
print(bids)

# COMMIT SESSION 
session.commit()

Base.metadata.create_all(engine)