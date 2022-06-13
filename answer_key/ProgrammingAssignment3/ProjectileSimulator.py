import csv
import math
import random


class ProjectileSimulator:

    def __init__(self, initialVelocityBounds: tuple, launchAngleBounds: tuple, gravity=-9.81):
        self.initialVelocityBounds = initialVelocityBounds
        self.launchAngleBounds = launchAngleBounds
        self.gravity = gravity

    def getRandomInitialVelocity(self) -> float:
        initialVelocity = random.uniform(self.initialVelocityBounds[0], self.initialVelocityBounds[1])
        return initialVelocity

    def getRandomLaunchAngle(self) -> float:
        launchAngle = random.uniform(self.launchAngleBounds[0], self.launchAngleBounds[1])
        return launchAngle

    @staticmethod
    def getInitialVerticalVelocity(initialVelocity: float, launchAngle: float) -> float:
        return initialVelocity * math.sin(math.radians(launchAngle))

    @staticmethod
    def getInitialHorizontalVelocity(initialVelocity: float, launchAngle: float) -> float:
        return initialVelocity * math.cos(math.radians(launchAngle))

    def getTimeOfFlight(self, initialVerticalVelocity: float) -> float:
        return -initialVerticalVelocity / (0.5 * self.gravity)

    @staticmethod
    def getLaunchDistance(initialHorizontalVelocity: float, timeOfFlight: float) -> float:
        return initialHorizontalVelocity * timeOfFlight

    def simulateLaunches(self, numLaunches: int) -> None:
        # Build object in memory to hold data table
        table = []
        headerRow = ["launch number", "launch angle", "initial velocity", "initial vertical velocity",
                     "initial horizontal velocity", "time of flight", "launch distance"]
        table.append(headerRow)
        # Simulate n launches, construct a row per launch, and append onto the table
        for n in range(numLaunches):
            trial = n + 1
            initialVelocity = self.getRandomInitialVelocity()
            launchAngle = self.getRandomLaunchAngle()
            verticalVelocity = self.getInitialVerticalVelocity(initialVelocity, launchAngle)
            horizontalVelocity = self.getInitialHorizontalVelocity(initialVelocity, launchAngle)
            timeOfFlight = self.getTimeOfFlight(verticalVelocity)
            launchDistance = self.getLaunchDistance(horizontalVelocity, timeOfFlight)
            row = [trial, launchAngle, initialVelocity, verticalVelocity, horizontalVelocity, timeOfFlight,
                   launchDistance]
            table.append(row)
        # Write the CSV file
        with open("projectileSimulations.csv", "w+", encoding="utf-8", newline="") as thisCSV:
            csvWriter = csv.writer(thisCSV)
            csvWriter.writerows(table)
