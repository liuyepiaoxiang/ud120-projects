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
    print('len', len(predictions))
    for i in range(len(predictions)):
        maxP.append(predictions[i])
        for j in range(len(predictions) / 10):
            maxindex = maxP.index(max(maxP))
            maxP.remove(max(maxP))
            ages.remove(ages[maxindex])
            net_worths.remove(net_worths[maxindex])
            predictions.remove(predictions[maxindex])

    cleaned_data = (ages, net_worths, predictions)
    return cleaned_data

