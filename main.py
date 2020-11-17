import requests
from flask import Flask, render_template,Response
import time
import datetime
import json


app = Flask(__name__)
URL_TUYA_API = "https://px1.tuyaus.com/homeassistant"

def tokenSwitch():
    auth = requests.post(
        "%s/auth.do" % URL_TUYA_API,
        data={
            "userName": "xxxxxx@gmail.com",
            "password": "xxxxxxxxxx",
            "countryCode": "1",
            "bizType": "tuya",
            "from": "tuya",
        },
    ).json()
    return auth["access_token"]


def switchTurn(token,switchId,status):
    print("TURNING %s" % status)
    r = requests.post(
        "%s/skill" % URL_TUYA_API,
        json={"header": {"name": "turnOnOff", "namespace": "control", "payloadVersion": 1}, "payload": {"accessToken": token, "devId": switchId, "value":"%d" % status}}
    ).json()

def statusSwitch(token,id):
    devices = requests.post(
        "%s/skill" % URL_TUYA_API,
        json={"header": {"name": "Discovery", "namespace": "discovery", "payloadVersion": 1}, "payload": {"accessToken": token}}
    ).json()
    device = next(dev for dev in devices["payload"]["devices"] if id in dev["id"])
    return device['data']['state']



@app.route('/switch')
def Switch():
    token = tokenSwitch()
    switchId = "xxxxxxxxxxx"
    status = 0
    try:
        if not statusSwitch(token,switchId):
            status = 1
    except Exception as e:
        pass

    switchTurn(token,switchId,status)
    return Response("%s" % status)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
