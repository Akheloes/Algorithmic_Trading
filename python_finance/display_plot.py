#!/usr/bin/env python

import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import numpy as np
import pandas_datareader.data as web 

df = pd.read_csv('../tsla.csv', parse_dates=True, index_col=0)

# print(df[['Open', 'Close']])

df[['Open', 'Close']].plot()
plt.show()