from backend.models import User, Event, Accident
import json
from flask import request
from backend import db

def get_all_accidents(filepath):
    file = open(filepath, 'r')
    file.readline()
    lines = file.readlines()
    for line in lines:
        data = [x.strip() for x in line.split(',')]
        year = int(data[13])
        month = int(data[12])
        day = int(data[11])
        weekday = int(data[14])
        hour = int(data[15])
        minute = int(data[16])
        lat = float(data[25])
        lon = float(data[26])
        new_accident = Accident(year=year, month=month, day=day, weekday=weekday, hour=hour, minute=minute, lat=lat, lon=lon)
        db.session.add(new_accident)
        if int(data[2]) % 500 == 0:
            print(data[2])
    db.session.commit()
