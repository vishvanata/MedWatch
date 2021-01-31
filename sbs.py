
import json
import random
import datetime
import boto3
import time

patientNames = ['Jack', 'Jane', 'Sam', 'Susan', 'Paul']

iot = boto3.client('iot-data');

# generate blood pressure values
def getFlowValues():
    data = {}
    data['Patient'] = random.choice(patientNames)
    data['Temperature'] = random.randint(95, 105)
    data['BloodPressure'] = (random.randint(80, 190), random.randint(50, 125))
    data['BreathRate'] = random.randint(10, 30)
    data['HeartRate'] = random.randint(40, 120)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# Generate each parameter's data input in varying proportions
while True:
    time.sleep(1)
    data = json.dumps(getFlowValues())
    print(data)
    response = iot.publish(
         topic='/sbs/devicedata/flow',
         payload=data
    )
