from ProjectileSimulator import ProjectileSimulator
from TextAnalyzer import TextAnalyzer
from WeatherChecker import WeatherChecker

# Text Analyzer Script
textAnalyzer = TextAnalyzer()
textAnalyzer.decryptTexts()
harryCount = textAnalyzer.countOccurrences("Harry")
print("Harry Count = " + str(harryCount))
textAnalyzer.replaceWord("Dursley", "Prune")
ronAndHermioneCount = textAnalyzer.countSameSentenceOccurrences("Ron", "Hermione")
print("Ron & Hermione Count = " + str(ronAndHermioneCount))

# Projectile Simulator Script
initialVelocityBounds = (0, 10)  # in meters/second (presumably)
launchAngleBounds = (0, 90)  # in degrees (presumably)
projectileSimulator = ProjectileSimulator(initialVelocityBounds, launchAngleBounds)
numLaunches = 1000  # User-defined number of launches to simulate
projectileSimulator.simulateLaunches(numLaunches)

# Weather Checker Script
weatherChecker = WeatherChecker()
weatherChecker.getBozemanWeather()
