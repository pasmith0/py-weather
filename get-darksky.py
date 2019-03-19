#!python3
# coding: iso-8859-15

# Documentation for DarkSkyAPI https://pypi.org/project/darkskyapi-py/
from DarkSkyAPI.DarkSkyAPI import DarkSkyClient
from datetime import date,timedelta
import json

api_key="090e7e665ad12cb36ef10e5fda751b1e"

# Denver lat/long
lat=39.742043
lon=-104.991531
# convert millibars to inches of Hg
MB_TO_INHG = 0.029530

# TODO: Add exclude here
client = DarkSkyClient(api_key, (lat, lon), units="us")

# To pretty print json
# print(json.dumps(client.daily.data[0],indent=4,sort_keys=True))

def deg_to_compass(deg):
    deg = deg % 360
    dir_arr = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    num_compass_headings = len(dir_arr)
    deg_per_compass_heading = 360/num_compass_headings
    val = int((deg/deg_per_compass_heading)+.5)
    return dir_arr[(val % num_compass_headings)]

def deg_to_compass2(deg):
    deg = deg % 360
    dir_arr = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    idx = int((deg + 11.25)/22.5) % len(dir_arr)
    return dir_arr[idx]


print("   Summary: " + client.raw_data['daily']['summary'])

wind_speed = int(client.currently.windSpeed+.5) # round the wind speed

print("   Now: %s %d°F, Wind %smph from %s, Humidity %d%%, Barometer %.2f" %\
      (client.currently.summary, int(client.currently.temperature+0.5),
      str(wind_speed),deg_to_compass2(client.currently.windBearing),
      client.currently.humidity*100,client.currently.pressure*MB_TO_INHG))

for i in range(3): # only want 3 days
   print("   %s: %s.. High %d°F, Low %d°F" % \
        (date.fromtimestamp(client.daily.data[i]['time']).strftime("%a"),\
         client.daily.data[i]['summary'], \
         client.daily.data[i]['temperatureHigh'], \
         client.daily.data[i]['temperatureLow']))
         
