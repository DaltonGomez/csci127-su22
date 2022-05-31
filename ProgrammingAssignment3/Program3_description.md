# Programming Assignment #3

### Instructions:

Please complete the questions/problems described here by creating the necessary `.py` files. Once completed,
submit the individual files of this directory to the Programming Assignment #3 submission box on
[Gradescope](https://www.gradescope.com/).

## Question #1 [50 Points]: Create a file `TextAnalyzer.py` that defines an object of the TextAnalyzer class, including:

**1a) A constructor that can be called as `TextAnalyzer()`. You do not need to create any attributes in the constructor,
but you can if you like.**

**1b) An instance method that can be called as `textAnalyzer.decryptTexts()`, which opens the file `cipher.txt` and
creates a dictionary to decrypt the text. Next, open all Harry Potter books with the ending `_encrypted.txt` and read
them in as a string. Then make a translation table using the string method `string.maketrans(decryptionDict)` and
finally translate the string using the method `string.translate(translationTable)`. Lastly, save each book as a
new text file with the book number and ending `_plain.txt`. You should be able to open that plaintext book and
read it!**

**1c) An instance method that can be called as `replaceWord(stringToFind: str, replacementString: str) -> None`. It
should read in all the plaintext books as strings and replace all occurrences of `stringToFind` with
`replacementString`. Finally, it should save each book as a new text file with the book number and ending
`_replaced.txt`. You should be able to open that replaced book and read it! (HINT: Use the method
`string.replace(old, new)`!)**

**1d) An instance method that can be called as `countOccurrences(stringToCount: str) -> int`. It should read in all
the plaintext books as strings and count all occurrences of `stringToCount`. Finally, it should return the integer
count. (HINT: Use the method `string.count(stringToCount)`! If this method is called on all seven books with the string
to count as `"Harry"`, you should get `18673`.)**

**1e) An instance method that can be called as `countSameSentenceOccurrences(firstString: str, secondString: str)
-> int`. It should read in all the plaintext books as strings and split on sentences. Then count all occurrences where
`firstString` and `secondString` are in the same sentence. Finally, it should return the integer count.
(HINT: Use the method `string.split(stringToSplitOn)`! If this method is called on all seven books with the first string
as `"Ron"` and the second string as `"Hermione"`, you should get `1645`.)**

**1f) A small amount of testing code at the end of the file that allows you to instantiate the `TextAnalyzer` class
and call these methods on an object.** **

## Question #2 [50 Points]: Create a file `ProjectileSimulator.py` that defines an object of the ProjectileSimulator class, including:

**2a) A constructor that can be called as `ProjectileSimulator(initialVelocityBounds: tuple, launchAngleBounds: tuple)`.
In the constructor, you should assign the tuples to instance attributes of the same name.**

**2b) An instance method that can be called as `projectileSimulator.getRandomInitialVelocity() -> float`, which should
randomly sample an initial velocity somewhere between the initial velocity bounds and return that velocity as
a float.n (HINT: Use the method `random.uniform(lowerBound, upperBound)`.)**

**2c) An instance method that can be called as `projectileSimulator.getRandomLaunchAngle() -> float`, which should
randomly sample an initial launch angle somewhere between the launch angle bounds and return that angle as
a float. (HINT: Use the method `random.uniform(lowerBound, upperBound)`.)**

**2d) An instance method that can be called as `projectileSimulator.getInitialVerticalVelocity(initialVelocity: float,
launchAngle: float) -> float`. This should calculate and return the initial velocity in the y-direction using
the following formula: `initialVerticalVelocity = initialVelocity * sine(launchAngle)`. (HINT: Use the method
`math.sin(input)`.)**

**2e) An instance method that can be called as `projectileSimulator.getInitialHorizontalVelocity(initialVelocity: float,
launchAngle: float) -> float`. This should calculate and return the initial velocity in the x-direction using
the following formula: `initialHorizontalVelocity = initialVelocity * cosine(launchAngle)`. (HINT: Use the method
`math.cos(input)`.)**

**2f) An instance method that can be called as `projectileSimulator.getTimeOfFlight(initialVerticalVelocity: float) ->
float`. This should calculate and return the time of flight using the following formula:
`timeOfFlight = initialVerticalVelocity / 4.905`.**

**2g) An instance method that can be called as `projectileSimulator.getLaunchDistance(initialHorizontalVelocity:
float, timeOfFlight: float) -> float`. This should calculate and return the horizontal distance that the projectile
traveled using the following formula: `launchDistance = initialHorizontalVelocity * timeOfFlight`.**

**2h) An instance method that can be called as `projectileSimulator.simulateLaunches(numLaunches: int) -> None`. This
should simulate `numLaunches` number of launches, where each launch you randomly sample a launch angle and
initial velocity, and calculate the initial vertical and horizontal velocities, the time of flight, and the
launch distance. Finally, save the results of all trials in a CSV file, where each trial is a row formatted as:
`[launch number, launch angle, initial velocity, initial vertical velocity, initial horizontal velocity, time of flight,
launch distance]`.**

**2i) A small amount of testing code at the end of the file that allows you to instantiate the `ProjectileSimulator`
class and call these methods on an object.**

## BONUS [+100 Points]: Create a file `WeatherChecker.py` that defines an object of the WeatherChecker class, including:

**BONUS PART 1) A constructor that can be called as `WeatherChecker(endpoint: str)`. In the constructor, you should
declare an
instance attributes called `self.endpoint` and assign the `endpoint` parameter to it. For the sake of this bonus,
the only endpoint you need to pass in is `"https://api.weather.gov/gridpoints/TFX/95,57/forecast"`, which is the
National Weather Service's REST API endpoint to check the weather for Bozeman, MT.**

**BONUS PART 2) An instance method that can be called as `weatherChecker.getBozemansWeather() -> None`. This should
use the library `requests` to make a `GET` request to the `endpoint`. Then use the library `json` to dump the response
and parse out the *MOST CURRENT* weather forecast for Bozeman. Print at least the `temperature` and `detailedForecast`
fields of the response.**
