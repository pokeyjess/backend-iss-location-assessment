#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import urllib.request
import time

# ASTRONAUTS


def get_astronauts():
    response = urllib.request.urlopen("http://api.open-notify.org/astros.json")
    result = json.loads(response.read())
    print("Total astronauts in space right now: " + str(result["number"]))
    astronauts = result["people"]
    for astronaut in astronauts:
        print("Name: " + astronaut["name"] +
              "\n \t Spacecraft: " + str(astronaut["craft"]))


get_astronauts()

# LOCATION


def get_location():
    response = urllib.request.urlopen(
        "http://api.open-notify.org/iss-now.json")
    result = json.loads(response.read())
    location = result["iss_position"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    print("Latitude: " + str(latitude) + "\nLongitude: " + str(longitude))


get_location()


def main():
    pass


if __name__ == '__main__':
    main()
