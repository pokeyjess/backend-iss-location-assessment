#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import requests
import time
#import argparse

astronaut_response = requests.get("http://api.open-notify.org/astros.json")
location_response = requests.get("http://api.open-notify.org/iss-now.json")
pass_time = requests.get("http://api.open-notify.org/iss-pass.json")


def get_timestamp():
    result = location_response.json()
    timestamp = result["timestamp"]
    print("As of " + time.ctime(timestamp) + ":")


get_timestamp()


def get_astronauts():
    result = astronaut_response.json()
    number = result["number"]
    print("There are " + str(number) + " astronauts in space")
    astronauts = result["people"]
    for astronaut in astronauts:
        print("Name: " + astronaut["name"] +
              "\n\t Spacecraft: " + astronaut["craft"])


get_astronauts()


def get_longitude():
    result = location_response.json()
    location = result["iss_position"]
    longitude = location["longitude"]
    return int(float(longitude))


def get_latitude():
    result = location_response.json()
    location = result["iss_position"]
    latitude = location["latitude"]
    return int(float(latitude))


print(f"The current location of the ISS is: \nLongitude: " + str(get_longitude()) +
      "\nLatitude: " + str(get_latitude()))


def create_map():
    map = turtle.Screen()
    map.setup(800, 400)  # width, height
    map.setworldcoordinates(-180, -90, 180, 90)
    map.bgpic("map.gif")
    map.register_shape("rocket.gif")


create_map()


def show_ISS_location():
    iss = turtle.Turtle()
    iss.shape("rocket.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(get_longitude(), get_latitude())


show_ISS_location()


turtle.done()  # last turtle command to keep graphic open

#result = pass_time.json()
# part D
# how to pass proper parameters for Indy into api through requests package
#lat, 40, long, -86
#pass_time - api

# time stamp -- use time.ctime()
# string/text on map that shows next date and time of pass over


def main():
    pass


if __name__ == '__main__':
    main()
