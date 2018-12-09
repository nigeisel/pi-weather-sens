 #!/bin/sh

#sudo python /home/pi/weather-sens/weather-check.py 60
sudo docker run --privileged nilsg/weather-extractor:1.0
