import pandas as pd

import numpy as npy


def outliers_iqr_mod(data, feature, left=1.5, right=1.5, log_scale=False):
    """
    Finding outliers in dataset using interquartile method.
    Classical iqr method was modified by adding options of using logarythmic scale and 
    manual input amount of interquartile intervals for both sides.
    
    Args: 
        data(Pandas.DataFrame) - dataset to use
        feature(str) - name of the basic feature to make research
        left(float, optional) - amount of interquartile intervals to the left. By default is set to 1.5
        right(float, optional) - amount of interquartile intervals to the right. By default is set to 1.5
        log_scale(Boolean, optional) - flag if to use logarythmic scale. By default is set to 'False'
    
    Returns:
        outliers(Pandas.DataFrame) - dataset of all outlying cases
        cleaned(Pandas.DataFrame) - dataset of cleaned data
    """
    if log_scale:
        x = npy.log(data[feature])
    else:
        x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
    return outliers, cleaned


def outliers_z_score_mod(data, feature, log_scale=False, left=3, right=3):
    """
    Finding outliers in dataset using z-score method.
    Classical z-score method was modified by adding options of using logarythmic scale and 
    manual input amount of interquartile intervals for both sides.
    
    Args: 
        data(pandas.DataFrame) - dataset to use
        feature(str) - name of the basic feature to make research
        left(float, optional) - amount of sigma intervals to the left. By default is set to 3
        right(float, optional) - amount of sigma intervals to the right. By default is set to 3
        log_scale(Boolean, optional) - flag if to use logarythmic scale. By default is set to 'False'
    
    Returns:
        outliers(pandas.DataFrame) - dataset of all outlying cases
        cleaned(pandas.DataFrame) - dataset of cleaned data
    """
    if log_scale:
        x = npy.log(data[feature]+1)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
    return outliers, cleaned

