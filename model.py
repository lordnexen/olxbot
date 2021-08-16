from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import query, sessionmaker

import config

engine = create_engine('sqlite:///advs.db', echo=True)
Base = declarative_base()

Session=sessionmaker(bind=engine)
session=Session()
session._model_changes = {}

class Advs(Base):
    
    session=Session()

    __tablename__ = "Advertisments"

    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    price = Column(String, nullable = False)
    url = Column(String, unique = True, nullable= False)
    location = Column(String, unique = False, nullable= False)
   
    def __init__(self, title, price, url, location):
        self.title = title
        self.price = price
        self.url = url
        self.location = location

    def __repr__(self):
        return f"{self.title},{self.url}"

Advs.metadata.create_all(engine)

def save_adv(title,url,location,price):
    
    news_exists = session.query(Advs).filter(Advs.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = Advs(title = title, url=url,location=location, price=price)
        Advs.session.add(new_news)

        Advs.session.commit()
        

              

