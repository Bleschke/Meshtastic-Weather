#! python
# getweather.py - it gets forecast from openweathermap.org website for today and the very next two days
# USAGE: python getweather.py [localization]
# XI 2020 Arnold Cytrowski
import json, requests, sys


if len(sys.argv) < 2:
    print('USAGE: python getweather.py [localization]')
    exit()

APPID = '07f4b682ff34ee2cd95a8e16e10de3f7'

location = ' '.join(sys.argv[1:])
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,
APPID)
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

w = weather_data['list']
print(f'Actual weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tommorow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('The day after tommorow, boi:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

print('aaand that\'s it')
