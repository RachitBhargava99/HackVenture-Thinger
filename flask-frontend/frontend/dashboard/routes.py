from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from flask_login import login_user, current_user, logout_user, login_required
import requests
import geocoder


dash = Blueprint('dash', __name__)

@dash.route('/', methods=['POST', 'GET'])
def dashboard():
    request_data = requests.post(current_app.config['ENDPOINT_ROUTE'] + current_app.config['ACCIDENT_COOR_DATA_URL'],
                                 json={'lat': geocoder.ip('me').latlng[0], 'lon': geocoder.ip('me').latlng[1]})
    data = request_data.json()
    if data['status'] == 0:
        flash(data['error'], 'danger')
        logout_user()
        return redirect(url_for('common.login'))
    elif data['status'] == 1:
        return render_template('dashboard.html', all_accident_points=data['accidents'])
