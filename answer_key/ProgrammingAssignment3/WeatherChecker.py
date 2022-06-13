import json

import requests


class WeatherChecker:

    def __init__(self):
        # NOTE: This URL is specifically for the forecast in Bozeman, MT
        self.nwsEndpoint = "https://api.weather.gov/gridpoints/TFX/95,57/forecast"
        self.location = "Bozeman, MT"

    def getBozemanWeather(self) -> None:
        """Hits the National Weather Service REST API endpoint for Bozeman, MT and prints the upcoming weather"""
        # Make API Request
        response = requests.get(self.nwsEndpoint)
        # Dump JSON payload
        weatherJSON = json.dumps(response.json(), indent=3)
        # Load JSON string into Python dictionary
        weatherDICT = json.loads(weatherJSON)
        # Dig into weather dictionary
        weatherProperties = weatherDICT["properties"]
        weatherPeriods = weatherProperties["periods"]
        upcomingWeather = weatherPeriods[0]
        timeOfDay = upcomingWeather["name"]
        temp = upcomingWeather["temperature"]
        forecast = upcomingWeather["detailedForecast"]
        # Build a nicely formatted string
        outputString = "\n=========== WEATHER FORECAST ===========\n"
        outputString = outputString + "\nWhat should you expect weather-wise in " + self.location + "?\n"
        outputString = outputString + "\nThe temperature for " + timeOfDay.lower() + " is " + str(temp) + " F.\n"
        charsThisLine = 0
        for charIdx in range(len(forecast)):
            outputString += forecast[charIdx]
            charsThisLine += 1
            if charsThisLine > 50 and forecast[charIdx] == " ":
                outputString += "\n"
                charsThisLine = 0
        # Print the weather report
        print(outputString)
