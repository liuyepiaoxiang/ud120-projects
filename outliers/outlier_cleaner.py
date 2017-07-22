#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    maxP = []
    for i in range(len(predictions)):
        maxP.append(predictions[i][0]-net_worths[i][0])
        cleaned_data.append((ages[i], net_worths[i], predictions[i]))
    for j in range(len(predictions) / 10):
        maxindex = maxP.index(max(maxP))
        maxP.remove(max(maxP))
        cleaned_data.remove(cleaned_data[maxindex])

    return cleaned_data

