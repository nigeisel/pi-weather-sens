import Adafruit_DHT
import time
import datetime
import sys
import json
from flask import Flask

sensor = Adafruit_DHT.DHT22
pin = 10

print("Starting server..")

app = Flask(__name__)

@app.route('/')
def weather():
    now = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    res = str(now) + "," + str(temperature) + "," + str(humidity)
    print(res)
    return res
