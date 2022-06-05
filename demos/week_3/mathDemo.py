import math
import random

launchAngle = 90 * random.random()  # In degrees, not radians
initialVelocity = 10 * random.random()

horizontalVelocity = initialVelocity * math.cos(math.radians(launchAngle))
