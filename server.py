#!/usr/bin/env python2.7

import os
from flask import Flask,render_template,abort,redirect,url_for,request,session
from database import db_session as db
from models import *

app=Flask(__name__)

def loggedin():
    username=session.get('user')
    password=session.get('pass')
    if username and password:
        user=db.query(User).filter_by(username=username).first()
        if user:
            if user.checkpass(password):
                session['id']=user.id
                return True
    return False

def setuser(name,pwd):
    session['user']=name
    session['pass']=pwd

@app.errorhandler(404)
def err404(err):
    return redirect(url_for('index'))

@app.route('/')
def index():
    if not loggedin():
        return redirect(url_for('login'))
    diaries=db.query(Diary).filter_by(owner=session['id']).all()
    return render_template('index.html',diaries=diaries)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    username=request.form['user']
    password=request.form['pass']
    setuser(username,password)
    if not loggedin():
        setuser('','')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    setuser('','')
    return redirect(url_for('index'))

@app.route('/diary/<name>')
def diary(name=''):
    if not loggedin():
        abort(403)
    d=db.query(Diary).filter_by(name=name,owner=session['id']).first()
    if not d:
        abort(404)
    ents=db.query(Entry).filter_by(diary=d.id).all()
    return render_template('diary.html',diary=d,entries=ents)

@app.route('/diary/<name>/addentry',methods=['POST'])
def addentry(name=''):
    if not loggedin():
        abort(403)
    d=db.query(Diary).filter_by(name=name,owner=session['id']).first()
    if not d:
        abort(404)
    e=Entry(d.id,request.form['text'])
    db.add(e)
    db.commit()
    return redirect(url_for('diary',name=name))

if __name__=='__main__':
    app.debug=True
    app.secret_key=os.urandom(64)
    app.run(host='127.0.0.1',port=1338)
