import datetime
from flask import request, Flask, send_file
from app import app, db
from app.models import TemperatureForDevice
from sqlalchemy import func
import uuid
import pandas as pd
from io import BytesIO
import openpyxl

@app.route('/heartbeat', methods=['GET'])
def hello():

    return 'OK', 200

@app.route('/reports/temperature', methods=['GET'])
def temperatureReport():

    timestamp = request.args.get('timestamp')

    # Validate parameter - Parameter not found
    if timestamp is None:
        return {"msg": "Parameter timestamp not found"}

    # grab data from Db and make - for demo use hardcoded values
    # temperatures = db.session.query(Temperature, Device).(Temperature.timestamp >= timestamp).all
    # .....

    location1 = uuid.uuid4()
    location2 = uuid.uuid4()
    results = []
    results.append(TemperatureForDevice(7, location1, datetime(2023, 3, 14, 12, 30, 00).timestamp(), 7.0))
    results.append(TemperatureForDevice(2, location2, datetime(2023, 3, 14, 12, 30, 00).timestamp(), 8.0))
    results.append(TemperatureForDevice(5, location1, datetime(2023, 3, 15, 12, 30, 00).timestamp(), 6.8))
    results.append(TemperatureForDevice(7, location1, datetime(2023, 3, 16, 12, 30, 00).timestamp(), 6.2))
    results.append(TemperatureForDevice(2, location2, datetime(2023, 3, 17, 12, 30, 00).timestamp(), 8.1))
    results.append(TemperatureForDevice(3, location2, datetime(2023, 3, 17, 12, 30, 00).timestamp(), 8.3))

    # fill dataframe with one row per object, one attribute per column
    df = pd.DataFrame([r.__dict__ for r in results])

    df1 = df.groupby(['device'], as_index=False).agg({'per_device': ['mean', 'min', 'max']})
    df2 = df.groupby(['location'], as_index=False).agg({'per_location': ['mean', 'min', 'max']})
    df3 = df.agg({'global': ['mean', 'min', 'max']})

    xlw = pd.ExcelWriter('result.xlsx', engine='openpyxl')
    df1.to_excel(xlw, sheet_name='per_device')
    df2.to_excel(xlw, sheet_name='per_location')
    df3.to_excel(xlw, sheet_name='global')

    file_stream = BytesIO()
    xlw.book.save(file_stream)
    file_stream.seek(0)

    return send_file(file_stream, attachment_filename="result.xlsx", as_attachment=True)