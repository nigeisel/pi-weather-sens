 #!/bin/sh

#sudo python /home/pi/weather-sens/weather-check.py 60
sudo docker run --privileged -d -e FLASK_APP=weather-server.py -p 5000:5000 nilsg/weather-extractor:1.1
