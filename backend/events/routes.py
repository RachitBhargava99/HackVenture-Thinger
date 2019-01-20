from flask import Blueprint, request
from backend.models import User, Event, Accident
from backend import db
import json
from sqlalchemy import and_
import gencoder
import requests
from backend import config

events = Blueprint('queues', __name__)


@events.route('/event', methods=['GET'])
def checker():
    return "Hello"


@events.route('/event/add', methods=['GET', 'POST'])
def add_event():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        lat = request_json['gps'][0]
        lon = request_json['gps'][1]
        user_id = user.id
        new_event = Event(lat=lat, lon=lon, user_id=user_id)
        db.session.add(new_event)
        db.session.commit()
        return json.dumps({'status': 1})


@events.route('/event/modify', methods=['GET', 'POST'])
def modify_event():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        type = request_json['type']
        curr_event = Event.query.filter_by(id=request_json['id'])
        curr_event.type = type
        db.session.commit()
        return json.dumps({'status': 1})


@events.route('/event/get', methods=['GET', 'POST'])
def get_unlogged_events():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        id = user.id
        event_ids = [x.id for x in Event.query.filter_by(user_id=id, type=-1)]
        return json.dumps({'status': 1, 'events': event_ids})


@events.route('/event/active', methods=['GET', 'POST'])
def get_active_events():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        id = user.id
        events = Event.query.filter(and_(Event.user_id != id, type == 0))
        curr_lat = request_json['gps'][0]
        curr_lon = request_json['gps'][1]
        event_ids = [{'id': x.id, 'lat': x.lat, 'lon': x.lon} for x in events if requests.post(
            f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={curr_lat},{curr_lon}&destinations=enc:{gencoder.polycoder.super_encoder([str(x.lat) + ', ' + str(x.lon)])}&key={config['MAPS_API_KEY']}").json()['rows'][0]['elements'][0]['distance']['value'] <= 5000]
        return json.dumps({'status': 1, 'events': event_ids})


@events.route('/event/list', methods=['GET', 'POST'])
def get_past_events():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        events = [{'id': x.id, 'lat': x.lat, 'lon':x.lon} for x in Event.query.filter_by(user_id=user.id)]
        return json.dumps({'status': 1, 'events': events})


@events.route('/event/all', methods=['GET', 'POST'])
def get_all_events():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0, 'error': "Authentication Failed"})
    else:
        event_ids = [{'id': x.id, 'lat': x.lat, 'lon': x.lon} for x in Event.query.filter_by(user_id=user.id)]
        return json.dumps({'status': 1, 'events': event_ids})


@events.route('/event/acc/all', methods=['GET', 'POST'])
def get_all_accidents():
    request_json = request.get_json()
    lat = request_json['lat']
    lon = request_json['lon']
    all_accidents = [{'lat': x.lat, 'lon': x.lon} for x in Accident.query.filter(and_(Accident.lat - lat <= 1,
                                                                                      Accident.lat - lat >= -1,
                                                                                      Accident.lon - lon <= 1,
                                                                                      Accident.lon - lon >= -1))]
    return json.dumps({'status': 1, 'accidents': all_accidents})
