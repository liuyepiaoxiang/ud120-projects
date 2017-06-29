#!/usr/bin/python
# -*- coding:utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# 数据的长度
print len(enron_data)
# 每个人的维度
print len(enron_data['METTS MARK'])
# 嫌疑人的数量
count = 0
poi = {}
for key in enron_data:
    if enron_data[key]['poi']==1:
        count+=1
        poi[count] = key
        print enron_data[key]
    print key
print count
print "poi", poi

lineCount = 0
poiCount = 0
enron_person = {}
poi_names = {}
with open('../final_project/poi_names.txt' , 'r') as f:
    for line in f.readlines():
        if lineCount>1:
            enron_person[lineCount-2] = line
            if enron_person[lineCount-2][1] == "y":
                poiCount+=1
                poi_names[poiCount] = enron_person[lineCount-2]
        lineCount+=1
print len(enron_person)
print "poiCount", poiCount
print "poi_names", poi_names

print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']


