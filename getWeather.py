#! python
# getWeather.py - gets current weather conditions from openweathermap.org website for and sends it over the Meshtastic Mesh
# USAGE: python getweather.py 
# Original Script by: 2020 Arnold Cytrowski, and geeksforgeeks.org
# Modified for Meshtastic by: 2024 Brian Leschke

import json, requests, sys, os

# Enter you API Key here
APPID = 'enter API key here'

# base_url
location = ' '.join(sys.argv[1:])
base_url ='"http://api.openweathermap.org/data/2.5/weather?'

# Enter City Latitude and Longitude
latitude = 'xx.xxxx'
longitude = '-xx.xxxx'

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&lat=" + latitude + "&lon=" + longitude

# get method of reponse object
# convert json format into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    fTemp = ((current_temperature - 273.15) * 9/5 + 32)

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    current_weather =  ("Current Weather in <your location>: " +
          "\n Conditions: " + str(weather_description) +
          "\n Temperature: " + str(round(fTemp, 2)) + " F" +
          "\n Humidity: " + str(current_humidity) + " %" +
          "\n Pressure: " + str(current_pressure) + " hPa")

    send_content = " ' " + current_weather + " ' "

    os.system("/usr/local/bin/meshtastic --ch-index 3 --sendtext" + send_content)

else:
    print(" City Not Found ")
