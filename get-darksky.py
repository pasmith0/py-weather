#!/bin/python3
# coding: iso-8859-15

# Documentation for DarkSkyAPI https://pypi.org/project/darkskyapi-py/
from DarkSkyAPI.DarkSkyAPI import DarkSkyClient
from datetime import date,timedelta

api_key="090e7e665ad12cb36ef10e5fda751b1e"

# Denver lat/long
lat=39.742043
lon=-104.991531

client = DarkSkyClient(api_key, (lat, lon), units="us")

print("Current: " + client.currently.summary + " " + \
      str(int(client.currently.temperature)) + "°F, " + \
      str(client.currently.humidity*100) + "% humidity, wind " + \
      str(client.currently.windSpeed) + "mph from " +\
      str(client.currently.windBearing))
for i in range(3):
   print("%s: %d°F - %d°F" % \
        (date.fromtimestamp(client.daily.data[i]['time']).strftime("%a"),\
         client.daily.data[i]['temperatureHigh'], \
         client.daily.data[i]['temperatureLow']))
         