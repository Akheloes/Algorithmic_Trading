#!/usr/bin/env python

import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import numpy as np
import pandas_datareader.data as web 

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2019, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)
head = df.head(7)

print(head)