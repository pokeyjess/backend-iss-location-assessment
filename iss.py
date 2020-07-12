#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import requests
import time
import argparse

# ASTRONAUTS


def get_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    result = response.json()
    number = result["number"]
    print("Total astronauts in space right now: " + str(number))
    astronauts = result["people"]
    for astronaut in astronauts:
        print("Name: " + astronaut["name"] +
              "\n\t Spacecraft: " + astronaut["craft"])


get_astronauts()

# LOCATION


def get_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    result = response.json()
    location = result["iss_position"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    print("Latitude: " + str(latitude) + "\nLongitude: " + str(longitude))


get_location()


map = turtle.Screen()
map.setup(800, 400)  # width, height
map.setworldcoordinates(-180, -90, 180, 90)
map.bgpic("map.gif")


turtle.done()  # last turtle command to keep graphic open

# part D
# how to pass proper parameters for Indy into api through requests package

# time stamp -- use time.ctime()
# string/text on map that shows next date and time of pass over


def main():
    pass


if __name__ == '__main__':
    main()
