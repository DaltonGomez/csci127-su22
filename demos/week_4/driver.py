from DataScientist import DataScientist

irisDS = DataScientist("water_potability")
irisDS.printDataFrame()
print(irisDS.getDataDescriptors())

irisDS.graphAllColumnHistograms()

irisDS.trainAndTestClassifier(cleanStrategy="replace", cleanStatistic="mean", testSize=0.20)
# unseenInstance = [5.2, 2.8, 4.1, 1.6]
# irisDS.classifyUnseenInstance(unseenInstance)
"""
# irisDS.graphColumnHistogram("sepal-length")
# irisDS.graphAllColumnHistograms()
irisDS.graphTwoColumnsAsScatterPlot("sepal-length", "sepal-width", runtimeRender=True)
print(irisDS.getNumpyArray())
print(irisDS.getColumnStatistic("mean", "sepal-length"))
print(irisDS.getQuery("`sepal-width`", "<", "2"))
print(irisDS.removeColumn("sepal-width"))
print(irisDS.removeIncompleteInstances())
print(irisDS.replaceIncompleteInstances("mean"))
"""
