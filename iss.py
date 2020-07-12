#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import requests
import time
#import argparse

astronaut_response = requests.get("http://api.open-notify.org/astros.json")
location_response = requests.get("http://api.open-notify.org/iss-now.json")
pass_time_response = requests.get(
    "http://api.open-notify.org/iss-pass.json?lat=40&lon=-86")


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


def get_pass_time():
    result = pass_time_response.json()
    pass_time = result["response"][1]["risetime"]
    print("The next time the ISS will pass over Indy will be: \n" +
          time.ctime(pass_time))


get_pass_time()

turtle.done()  # last turtle command to keep graphic open


# mark Indy with yellow dot
# print time of flyover next to yellow dot


def main():
    pass


if __name__ == '__main__':
    main()
