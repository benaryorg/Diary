#!/usr/bin/env python2.7

from sqlalchemy import Column,Integer,String
from database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True,unique=True)
    username=Column(String(256),unique=True)
    password=Column(String(128))
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
