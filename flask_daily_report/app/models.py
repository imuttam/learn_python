from app import db, app
from datetime import datetime

class Report(db.Model):
    id =        db.Column(db.Integer, primary_key=True)
    date =      db.Column(db.DateTime)
    voice_2G  = db.Column(db.Integer,  nullable=False)
    voice_3G  = db.Column(db.Integer, nullable=False)
    volte =     db.Column(db.Float, nullable=False)
    data_2G =   db.Column(db.Float, nullable=False)
    data_3G =   db.Column(db.Float, nullable=False)
    data_4G =   db.Column(db.Float, nullable=False)
    vlrcount =  db.Column(db.Integer,  nullable=False)
    total_voice = db.Column(db.Integer,  nullable=False)
    total_data = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f"Report('{self.date}', '{self.total_voice}', {self.total_data})"
