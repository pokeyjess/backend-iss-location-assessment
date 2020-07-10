#!/usr/bin/env python

__author__ = 'pokeyjess'

import json
import turtle
import urllib.request
import time


api = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(api)
result = json.loads(response.read())
print("Astronauts in space: " + str(result["number"]))


def main():
    pass


if __name__ == '__main__':
    main()
