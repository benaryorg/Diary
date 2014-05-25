#!/usr/bin/env python2.7

import getpass
from models import *
from database import db_session as db

passprompt=lambda:(getpass.getpass('Password: '),getpass.getpass('Retype password: '))

if __name__=='__main__':
    username=raw_input('Username: ')
    p1,p2=passprompt()
    while p1!=p2:
        print 'Passwords do not match!'
        p1,p2=passprompt()
    db.add(User(username,p1))
    db.commit()
