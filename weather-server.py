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
    if temperature < 20:
        temp_color = "blue"
    elif temperature > 26:
        temp_color = "red"
    else:
        temp_color = "black"

    if humidity < 35 or humidity > 75:
        humidity_color = "red"
    else:
         humidity_color = "black"

    html = """
    <html><body>
        <h2>Sensors</h2>
        <p style="color:{temp_color}">Temperature: {temp}C</p>
        <p style="color:{humidity_color}">Humidity: {humidity}&#37;</p>
    </body></html>
    """.format(temp=temperature, temp_color=temp_color, humidity=humidity, humidity_color=humidity_color)
    
    return res
