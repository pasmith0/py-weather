#!/bin/python3
# coding: iso-8859-15

# Documentation for DarkSkyAPI https://pypi.org/project/darkskyapi-py/
from DarkSkyAPI.DarkSkyAPI import DarkSkyClient
from datetime import date,timedelta

api_key="090e7e665ad12cb36ef10e5fda751b1e"

# Denver lat/long
lat=39.742043
lon=-104.991531
# convert millibars to inches of Hg
MB_TO_INHG = 0.029530

client = DarkSkyClient(api_key, (lat, lon), units="us")

#printf "  Now: %-#{width}s %.0f°%s, Wind %s, Humidity %s, Barometer %s %s\n", 
print("Summary: " + client.raw_data['daily']['summary'])
#print("Now: " + client.currently.summary + " " + \
#      str(int(client.currently.temperature+0.5)) + "°F, " + \
#      "Wind " + str(client.currently.windSpeed) + "mph bearing " + \
#      str(client.currently.windBearing) + \
#      ", Humidity " + str(client.currently.humidity*100) + "% " + \
#      ", Barometer " + str(client.currently.pressure*MB_TO_INHG))
print("Now: %s %d°F, Wind %smph from %s, Humidity %d%%, Barometer %.2f" %\
      (client.currently.summary, int(client.currently.temperature+0.5),
      str(client.currently.windSpeed),str(client.currently.windBearing),
      client.currently.humidity*100,client.currently.pressure*MB_TO_INHG))

for i in range(3):
   print("%s: %d°F - %d°F" % \
        (date.fromtimestamp(client.daily.data[i]['time']).strftime("%a"),\
         client.daily.data[i]['temperatureHigh'], \
         client.daily.data[i]['temperatureLow']))
         