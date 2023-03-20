from app import db
from sqlalchemy.dialects.postgresql import UUID

class Device(db.Model):
    __tablename__ = 'Device'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(UUID(as_uuid=True), nullable=False)

    def __repr__(self):
        return f'<Device {self.id} {self.location_id}>'
    

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer, db.ForeignKey('Device.Id'), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False, Index=True)
    value = db.Column(db.Numeric(10,2), nullable=False)

    def __repr__(self):
        return f'<Temperature {self.id} {self.device_id} {self.timestamp} {self.value}>'    
    
class TemperatureForDevice():
    def __init__(self, device, location, timestamp, value):
        self.device = device
        self.location = location
        self.timestamp = timestamp
        self.value = value

    