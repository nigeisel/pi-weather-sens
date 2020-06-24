FROM resin/raspberry-pi-python:2-slim

WORKDIR /app

#RUN apk add git
#RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#RUN cd Adafruit_Python_DHT && python setup.py install
RUN pip install Adafruit_DHT
RUN pip install Flask

RUN mkdir data && touch data/data.csv

COPY  API_KEY ./
COPY weather-check.py ./
COPY weather-server.py ./

# ENTRYPOINT ["python", "weather-check.py", "60"]
ENTRYPOINT ["export", "FLASK_APP=weather-server.py", "flask", "run"]
