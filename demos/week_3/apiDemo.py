import json

import requests

endpoint = "https://api.weather.gov/gridpoints/TFX/95,57/forecast"

response = requests.get(endpoint)
print(response)
print(type(response))
weatherDict = response.json()
print(weatherDict)
print(type(weatherDict))

weatherStr = json.dumps(weatherDict, indent=3)
print(weatherStr)
print(type(weatherStr))

properties = weatherDict["properties"]
periods = properties["periods"]
print(periods)
print(type(periods))
mostRecentForecast = periods[0]
print(mostRecentForecast)
print(type(mostRecentForecast))
mostRecentForecastStr = json.dumps(mostRecentForecast, indent=3)
print(mostRecentForecastStr)
