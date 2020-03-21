from pymongo import MongoClient
from datetime import date, datetime
import blood_oxygen
import pulse

client = MongoClient("mongodb+srv://ec500:ruby@cluster0-092qv.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("ec500-HW5")
records = db.heartRateMonitor

def create():
    new_patient = {
        'createAt': str(datetime.now()),
        'pulse':pulse.read_pulse(),
        'bloodOx':blood_oxygen.read_blood_oxygen(),
        'bloodPre':'120/90'
    }
    records.insert_one(new_patient)

create()    