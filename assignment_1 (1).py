# -*- coding: utf-8 -*-
"""Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NK3lGwI2COjLwb-obMFj_jg-_ig0nbNw
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

"""## File Q9_a"""

from google.colab import files
upload = files.upload()

cal=pd.read_csv("Q9_a (1).csv")

cal.head()

"""## Skewness"""

cal.skew()

"""##  Kurtosis"""

cal.kurtosis()

cal.hist()

"""## File Q9_B"""

from google.colab import files
upload = files.upload()

spwt=pd.read_csv("Q9_b.csv")

spwt.head()

"""## Skewness"""

spwt.skew()

"""## Kurtosis"""

spwt.kurtosis()

spwt.hist()

spwt.describe()

"""## Q 12"""

x = (34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56)

import statistics as stats

print('mean',stats.mean(x))
print('median',stats.median(x))
print('variance',stats.variance(x))
print('standard deviation', stats.stdev(x))

"""## Q 21"""

from google.colab import files
upload = files.upload()

cars=pd.read_csv("Cars.csv")

cars.head()

cars.describe()

cars.mean()

cars.std()

cars.median()

cars.mode()

"""## Q 20"""

from scipy import stats

stats.norm.cdf(38,34.42,9.13)

stats.norm.cdf(38,34.42,9.13)

stats.norm.cdf(20,34.42,9.13)

stats.norm.cdf(50,34.42,9.13)

(stats.norm.cdf(50,34.42,9.13))-(stats.norm.cdf(20,34.42,9.13))

"""## Q 21 B"""

from google.colab import files
upload = files.upload()

wcat=pd.read_csv("wc-at.csv")

wcat.head()

wcat.mean()

wcat.median()

wcat.mode()

