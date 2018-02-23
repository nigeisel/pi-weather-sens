import Adafruit_DHT
import time
import datetime

INTERVAL = 30 * 60
DATA_FILE = "data"

try:
	file = open(DATA_FILE, 'r')
except IOError:
	file = open(DATA_FILE, 'w')
	file.write("Date,Temperature,Humidity")

while True:
	sensor = Adafruit_DHT.DHT22
	pin = 10
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	now = datetime.datetime.now()
		
	#persist
	with open(DATA_FILE, "a") as data_file:
		data_file.write(now + "," + temperature + "," + humidity)

	#wait interval
	time.sleep(interval)
