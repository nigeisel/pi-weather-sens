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
    temp_color = temperature < 20 ? "blue" : (temperature > 25 "red" : "black")
    humidity_color = (humidity > 75 OR humidity < 35) ? "red" : "black"
    html = """
    <html><body>
        <h2>Sensors</h2>
        <p style="color:{temp_color}">Temperature: {temp}C</p>
        <p style="color:{humidity_color}">Humidity: {humidity}&#37;</p>
    </body></html>
    """.format(temp=temperature, temp_color=temp_color, humidity=humidity, humidity_color=humidity_color)
    return res
