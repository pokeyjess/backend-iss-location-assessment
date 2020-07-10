#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import urllib.request
import time

# ASTRONAUTS
response = urllib.request.urlopen("http://api.open-notify.org/astros.json")
result = json.loads(response.read())
print("Total astronauts in space right now: " + str(result["number"]))
astronauts = result["people"]
for astronaut in astronauts:
    print("Name: " + astronaut["name"] +
          "\n \t Spacecraft: " + str(astronaut["craft"]))
# LOCATION
response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
result = json.loads(response.read())
location = result["iss_position"]
latitude = location["latitude"]
longitude = location["longitude"]
print("Latitude: " + str(latitude) + "\nLongitude: " + str(longitude))


def main():
    pass


if __name__ == '__main__':
    main()
