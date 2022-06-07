# Programming Assignment #4

### Instructions:

Please complete the questions/problems described here by creating the necessary `.py` files. Once completed,
submit the individual files of this directory to the Programming Assignment #4 submission box on
[Gradescope](https://www.gradescope.com/).

## Question #1 [25 Points]: ML Step 1: Read-In Data (and Basic Operations)

**1a) Create a file named `DataScientist.py` that defines an object of the `DataScientist` class. The constructor of the
`DataScientist` class should be able to be called as `DataScientist(datasetName: str)`. In the constructor, you should
assign the `datasetName` to an instance attribute called `self.datasetName`. Additionally, you should have an instance
attribute called `self.dataFrame` that is assigned the Pandas dataframe object returned by reading in the corresponding
CSV file in the constructor. Lastly, you should have an instance attribute called `self.classifier` that is initialized
with the `None` datatype.**

**1b) Include an instance method that can be called as `printDataframe() -> None`. This should simply print the Pandas
dataframe stored in the `DataScientist` object.**

**1c) Include an instance method that can be called as `getDataAsNumpyArray() -> ndarray`. This should return the Numpy
array version of the Pandas dataframe.**

**1d) Include an instance method that can be called as `printDataDescriptors() -> None`. This should print the
descriptive statistics of the dataset as its own Pandas dataframe, as well as the shape and columns of the dataset.**

**1e) Include an instance method that can be called as `getColumnStatistic(stat: str, column: str) -> float`. This
should return the specified statistic for a specified column of the dataset. Note that the descriptive statistics are
one of the following: `[count, mean, std, min, 25%, 50%, 75%, max]`.**

**1f) Include an instance method that can be called as `getDataSortedByColumn(column: str) -> DataFrame`. This should
return a new Pandas dataframe where the instances (i.e. rows) have been sorted by the values in a specified column.**

**1g) Include an instance method that can be called as `getQuery(column: str, boolOperator: str, value: str) ->
DataFrame`. This should return a new Pandas dataframe that only includes instances which match the query. Note that the
query is built by concatenating `column + boolOperator + value`. For example, `iris.getQuery("petal_length", ">", "2")`
would return all instances where the `petal_length` feature is greater than 2.**

## Question #2 [25 Points]: ML Step 2: Clean Data

**2a) Include an instance method that can be called as `removeColumn(column: str) -> DataFrame`. This should return a
new Pandas dataframe with everything except the specified column.**

**2b) Include an instance method that can be called as `removeIncompleteInstances() -> DataFrame`. This should return a
new Pandas dataframe where all instances with a single missing value have been removed.**

**2c) Include an instance method that can be called as `replaceIncompleteInstances(stat: str) -> DataFrame`. This
should return a new Pandas dataframe where all instances with a missing value have had their missing value replaced by
the specified statistic of that column. (HINT: You may have to iterate over the `dataFrame.columns` and call the
`getColumnStatistic(stat, column)` method.)**

## Question #3 [25 Points]: ML Step 3: Visualize Data

**3a) Include an instance method that can be called as `graphColumnHistogram(column: str, bins=12) -> None`. This
should create a single figure that contains a histogram for each label in the dataset on the column. The `bins=` keyword
argument should specify the number of "rectangles" you'd like the histogram to have (12 is a good default option). The
histogram should get saved to the path: `"figs/" + self.datasetName + "_hist_" + column + ".png"`**

**3b) Include an instance method that can be called as `graphAllHistograms(bins=12) -> None`. This should create the
histograms described in 2a for every column in the dataset, saving each to the `figs/` directory.**

**3c) Include an instance method that can be called as `graphTwoColumnsAsScatterPlot(xAxisColumn: str, yAxisColumn: str)
-> None`. This should create a single figure that contains a scatter plot for the two columns label in the dataset. The
scatter plot should get saved to the path: `"figs/" + self.datasetName + "_scatter_" + xAxisColumn + "_" + yAxisColumn +
".png"`**

**3d) Include an instance method that can be called as `graphAllPairwiseScatterPlots(self) -> None`. This should create
the scatter plots described in 2b for pairwise combination of columns in the dataset, saving each to the `figs/`
directory.**

## Question #4 [25 Points]: ML Step 4: Learn a Model and Deploy

**4a) Include an instance method that can be called as `trainAndTestClassifier(self, cleaning="replace",
replacementStat="mean", testSize=0.25) -> None`. This first clean the data using either the `removeIncompleteInstances()
-> DataFrame` method or the `replaceIncompleteInstances(stat: str) -> DataFrame` method. The cleaning method should be
specified by the keyword argument `cleaning=`, and the statistic used for replacement should be specified by the keyword
argument `replacementStat=`. Next, you should get the dataframe as a Numpy array and split it into two sub-arrays, one
for the features and one for the labels. Then use the SciKit-Learn `train_test_split` function to randomly generate the
tuple of `(trainFeatures, testFeatures, trainLabels, testLabels)`. Now, you can assign the uninitialized
`self.classifier` attribute to be a SciKit-Learn machine learning model. For this assignment, let's use a support vector
machine (SVM), which can be instantiated with the line `self.classifier = svm.SVC()`. Next, you can train or "fit"
the model to the training data with `self.classifier.fit(trainFeatures, trainLabels)`. Finally, you can test the
accuracy of this ML model on this dataset by calling `accuracy = self.classifier.score(testFeatures, testLabels)`. The
value returned to accuracy is a number between 0 and 1 that can be interpreted as the percent of unseen (i.e. test
instances) that were correctly labeled. Print this accuracy to the user!**

**4b) Include an instance method that can be called as `classifyUnseenInstance(instanceFeatures: list) -> int`. This
method should take in a single unseen/unknown instance's features and call the method `classification =
self.classifier.predict(instanceFeatures)`. The label (which in all of our datasets is an integer that maps to the true
label) is returned and assigned to the `classification` variable. Note that you must take care to match the length of
your input `instanceFeatures` to the dataset or else the model won't be able to process it.
You should print and return the `classification`.**

**4c) Create a new file `driver.py` that allows you to instantiate the `DataScientist` class many times over on
specified datasets and call the methods you've written on those `DataScientist` objects. Use this file to test your
class/methods. And with that... Congratulations! You just built a machine learning pipeline!!!**

## BONUS: [+50 Points]: Beyond the Basics

**Create a file called `AdvancedDataScientist.py` that defines an object of the `AdvancedDataScientist` class.
In this class, create the necessary methods to read-in clean, visualize, and train a model for the `rain_tomorrow`
dataset. Note that all the other datasets contain only numerical data. That is not the case with this one. As such,
you'll need to familiarize yourself with working with other data types in ML pipelines.**
