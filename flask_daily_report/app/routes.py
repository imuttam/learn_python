from flask import render_template, url_for, flash, redirect,request
from app import app,db
from app.models import Report
import datetime

now = datetime.datetime.now()
today = now.strftime('%A , %d-%B-%Y')

counter = 0
@app.route('/')
@app.route('/')
def index():
    global counter
    counter +=1
    # report = Report.query.all()
    report = Report.query.order_by(Report.date.desc()).all()
    return render_template('index.html', title='Home', utc_dt=today,counter=counter,report=report)

# @app.route('/')
# def home():
#     return render_template('home.html')

