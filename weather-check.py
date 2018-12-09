import Adafruit_DHT
import time
import datetime
import sys
import json
import requests

if len(sys.argv) > 1:
  INTERVAL = float(sys.argv[1]) * 60
else:
  INTERVAL = 60 * 60

DATA_FILE = "data/data.csv"

# API
API_KEY = open('API_KEY', 'r').read().strip()
API_URL = "https://api.thingspeak.com/update.json"

sensor = Adafruit_DHT.DHT22
pin = 10

try:
  file = open(DATA_FILE, 'r')
except IOError:
  file = open(DATA_FILE, 'w')
  file.write("Date,Temperature,Humidity")

print("Starting extraction..")

while True:
  now = datetime.datetime.now()

  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  print(str(now) + "," + str(temperature) + "," + str(humidity))
  r = requests.post(API_URL, headers={"THINGSPEAKAPIKEY": API_KEY}, params={'field2': temperature, 'field3': humidity})
  try:
    r.raise_for_status()
  except requests.exceptions.HTTPError as e:
    print(e)


  with open(DATA_FILE, "a") as data_file:
    data_file.write("\n" + str(now) + "," + str(temperature) + "," + str(humidity))

  print("Time: " + str(now) + " --- Temperature: " + str(temperature) + ", Humidity: " + str(humidity))

  time.sleep(INTERVAL)

