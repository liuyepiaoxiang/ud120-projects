#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

## print "the length of feature_train now is ",len(features_train)
## print "the length of label_train now is ",len(labels_train)
## print "After,the length of feature_train now is ",len(features_train)
## print "After,the length of label_train now is ",len(labels_train)


#########################################################
### your code goes here ###
import numpy as np
from sklearn import svm
from sklearn.metrics import  accuracy_score
## features_train = features_train[:len(features_train)/100]
## labels_train = labels_train[:len(labels_train)/100]

## linear
clf_l = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_l.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_l = clf_l.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_l)
print "the accuracy of linear is",accuracy_score(pred_l,labels_test)

## rbf 1.0
clf_r = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r = clf_r.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r)
print "the accuracy of rbf is",accuracy_score(pred_r,labels_test)

## rbf 10.0
clf_r10 = svm.SVC(C=10.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r10.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r10 = clf_r10.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r10)
print "the accuracy of rbf10 is",accuracy_score(pred_r10,labels_test)


## rbf 10000.0
clf_r10000 = svm.SVC(C=10000.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r10000.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r10000 = clf_r10000.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r10000)
print "the accuracy of rbf10000 is",accuracy_score(pred_r10000,labels_test)
#########################################################

## less data
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
print "################################" \
      "less data "
## linear
clf_l = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_l.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_l = clf_l.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_l)
print "the accuracy of linear is",accuracy_score(pred_l,labels_test)

## rbf 1.0
clf_r = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r = clf_r.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r)
print "the accuracy of rbf is",accuracy_score(pred_r,labels_test)

## rbf 10.0
clf_r10 = svm.SVC(C=10.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r10.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r10 = clf_r10.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r10)
print "the accuracy of rbf10 is",accuracy_score(pred_r10,labels_test)


## rbf 100.0
clf_r100 = svm.SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r100.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r100 = clf_r100.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r100)
print "the accuracy of rbf100 is",accuracy_score(pred_r100,labels_test)


## rbf 1000.0
clf_r1000 = svm.SVC(C=1000.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r1000.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r1000 = clf_r1000.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r1000)
print "the accuracy of rbf1000 is",accuracy_score(pred_r1000,labels_test)

## rbf 10000.0
clf_r10000 = svm.SVC(C=10000.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma=1.0, kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

t0 = time()
clf_r10000.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred_r10000 = clf_r10000.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
accuracy_score(labels_test,pred_r10000)
print "the accuracy of rbf10000 is",accuracy_score(pred_r10000,labels_test)
print "the element of 10 is",pred_r10000[10]
print "the element of 26 is",pred_r10000[26]
print "the element of 50 is",pred_r10000[50]


