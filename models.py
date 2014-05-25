#!/usr/bin/env python2.7

import datetime,bcrypt

from sqlalchemy import Column,Integer,String,Date
from database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True,unique=True)
    username=Column(String(256),unique=True)
    password=Column(String(128))
    
    def __init__(self,username,password):
        self.username=username
        self.password=bcrypt.hashpw(password.encode(),bcrypt.gensalt().encode())

    def checkpass(self,password):
        return self.password==bcrypt.hashpw(password.encode(),self.password.encode())

class Diary(Base):
    __tablename__='diaries'
    id=Column(Integer(),primary_key=True,unique=True)
    owner=Column(Integer())
    name=Column(String(256),unique=True)

    def __init__(self,owner,name):
        self.owner=owner
        self.name=name

class Entry(Base):
    __tablename__='entries'
    id=Column(Integer(),primary_key=True,unique=True)
    diary=Column(Integer())
    date=Column(Date())
    text=Column(String(8192))

    def __init__(self,diary,text):
        self.diary=diary
        self.text=text
        #self.date=datetime.datetime.now().strftime("%Y-%m-%d")
        self.date=datetime.datetime.now()
