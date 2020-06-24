 #!/bin/sh

#sudo python /home/pi/weather-sens/weather-check.py 60
sudo docker run --privileged -d -p 8080:5000 nilsg/weather-extractor:1.0
