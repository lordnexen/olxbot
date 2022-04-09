from enum import unique
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
    chat_id = Column(Integer,nullable = False)
    title = Column(String, nullable = False)
    price = Column(String, nullable = False)
    url = Column(String, unique = True, nullable= False)
    location = Column(String, unique = False, nullable= False)
   
    def __init__(self, title, price, url, location, chat_id):
        self.title = title
        self.price = price
        self.url = url
        self.location = location
        self.chat_id = chat_id

    def __repr__(self):
        return f"{self.title},{self.url}"

Advs.metadata.create_all(engine)


def save_adv(title,url,location,price,chat_id):
    
    news_exists = session.query(Advs).filter(Advs.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = Advs(title = title, url=url,location=location, price=price, chat_id=chat_id)
        Advs.session.add(new_news)

        Advs.session.commit()
        

              

