from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///wow.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_name = Column(String, primary_key = True)
    login = Column(String)
    server = Column(String)
    def __init__(self, user_name, login, server):
        """"""
        self.user_name = user_name
        self.login = login
        self.server = server
    
class Guild(Base):
    __tablename__ = 'guild'
    user_name = Column(String, primary_key = True)
    guild = Column(String)
    server = Column(String)
    def __init__(self, user_name, guild, server):
        """"""
        self.user_name = user_name
        self.guild = guild
        self.server = server
    
class Item(Base):
    __tablename__ = 'item'
    user_name = Column(String, primary_key = True)
    item = Column(String)
    server = Column(String)
    def __init__(self, user_name, item, server):
        """"""
        self.user_name = user_name
        self.item = item
        self.server = server

Base.metadata.create_all(engine)
