import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-61291-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')


data = {
    "123456":
        {
            "name": "Kunal Dewangan",
            "major": "CSE",
            "Starting_year": 2019,
            "total_attendance": 10,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-05-23 00:54:34"
        },
    "702356":
        {
            "name": "Sandeep Suryawanshi",
            "major": "CSE",
            "Starting_year": 2019,
            "total_attendance": 8,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-05-23 00:54:34"
        },
    "789654":
        {
            "name": "Vinay Kumar Sahu",
            "major": "CSE",
            "Starting_year": 2019,
            "total_attendance": 9,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-05-23 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "CSE",
            "Starting_year": 2019,
            "total_attendance": 10,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-05-23 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
