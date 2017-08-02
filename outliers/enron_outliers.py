#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
print data_dict
data_dict.pop( 'TOTAL', 0 )
data_dict.pop( 'FREVERT MARK A', 0 )
data_dict.pop( 'LAY KENNETH L', 0 )
data_dict.pop( 'LAVORATO JOHN J', 0 )
data_dict.pop( 'SKILLING JEFFREY K', 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# LAY, KENNETH L      FREVERT, MARK A   LAVORATO, JOHN J    SKILLING, JEFFREY K
# FREVERT MARK A  LAY KENNETH L  LAVORATO JOHN J   SKILLING JEFFREY K
