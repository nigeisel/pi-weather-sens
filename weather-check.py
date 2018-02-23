import Adafruit_DHT
import time
import datetime
import sys
import json

if len(sys.argv) > 1:
	INTERVAL = float(sys.argv[1]) * 60
else:
	INTERVAL = 60 * 60

DATA_FILE = "data/data.csv"

sensor = Adafruit_DHT.DHT22
pin = 10

try:
	file = open(DATA_FILE, 'r')
except IOError:
	file = open(DATA_FILE, 'w')
	file.write("Date,Temperature,Humidity")


while True:

	now = datetime.datetime.now()

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print(str(now) + "," + str(temperature) + "," + str(humidity))
		
	with open(DATA_FILE, "a") as data_file:
		data_file.write("\n" + str(now) + "," + str(temperature) + "," + str(humidity))

	time.sleep(INTERVAL)
