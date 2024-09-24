import csv
from app import app, db
from app.models import Report
from datetime import datetime


app.app_context().push()

with open('report.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Convert the date string to a datetime object
        date_str = row['date']
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        report_instance = Report(
            date=date_obj,
            voice_2G=int(row['voice_2G']),
            voice_3G=int(row['voice_3G']),
            volte=float(row['volte']),
            data_2G=float(row['data_2G']),
            data_3G=float(row['data_3G']),
            data_4G=float(row['data_4G']),
            vlrcount=int(row['vlrcount']),
            total_voice=int(row['total_voice']),
            total_data=float(row['total_data'])
        )
        db.session.add(report_instance)

db.session.commit()
