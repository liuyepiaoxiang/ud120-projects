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
        maxP[i] = predictions[i][0]
        for j in range(len(predictions) / 10):
            maxindex = maxP.index(max(maxP))
            maxP.remove(max(maxP))
            cleaned_data[i] = (ages[maxindex], net_worths(maxindex), predictions[maxindex])

    return cleaned_data

