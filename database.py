#!/usr/bin/env python2.7

from sqlalchemy import create_engine,event,exc
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///sqlite.db',convert_unicode=True)
db_session=scoped_session(sessionmaker(autocommit=False,autoflush=True,bind=engine))
Base=declarative_base()
Base.query=db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

if __name__=='__name__':
    init_db()
