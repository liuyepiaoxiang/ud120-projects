#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
### KNN algorithm
### TODO:该算法还未实现
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.metrics import accuracy_score
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
nbrs.fit(features_train, labels_train)
#nbrs_score = cross_val_score(nbrs,features_test)
#predict_knn = nbrs.predict(features_test)
#accuracy_score_knn = accuracy_score(labels_test,predict_knn)
#print 'accuracy_score_knn:', accuracy_score_knn
#print 'accuracy_score_mean_nbrs:', nbrs_score.mean()

### adaboost algorithm
from sklearn.ensemble import AdaBoostClassifier

adab = AdaBoostClassifier(n_estimators= 100)
#adab.fit(features_train,labels_train)
adaa_score = cross_val_score(adab,features_train,labels_train)
##predict_adab = adab.predict(features_test)
##accuracy_score_adab = accuracy_score(features_test)
##print 'accuracy_score_adab:', accuracy_score_adab
print 'accuracy_score_mean_adab:', adaa_score.mean()



### Random forest algorithm
from sklearn.ensemble import RandomForestClassifier
rmf = RandomForestClassifier(n_estimators=10)
rmf.fit(features_train,labels_train)
#rmf_score = cross_val_score(rmf,features_test)
predict_rmf = rmf.predict(features_test)
accuracy_score_rmf = accuracy_score(labels_test,predict_rmf)
print 'accuracy_score_rmf:', accuracy_score_rmf
#print 'accuracy_score_mean_rmf:', rmf_score.mean()

try:
    #prettyPicture(nbrs, features_test, labels_test)
    #prettyPicture(adab, features_test, labels_test)
    prettyPicture(rmf, features_test, labels_test)
except NameError:
    pass
