#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import urllib.request
import time


api = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(api)
result = json.loads(response.read())
print("Total astronauts in space right now: " + str(result["number"]))
astronauts = result["people"]
for astronaut in astronauts:
    print("Name: " + astronaut["name"] +
          "\n \t Spacecraft: " + str(astronaut["craft"]))


def main():
    pass


if __name__ == '__main__':
    main()
