import pandas as pd


import pandas_datareader.data as GetData
df = GetData.get_data_yahoo("IBM")

#If we want to achieve a period
import datetime
dateBeg = datetime.datetime(2019, 9, 18)
dateEnd = datetime.datetime(2020, 9, 18)
df = GetData.get_data_yahoo("IBM", dateBeg, dateEnd)

#With this way we can know the percents change
import numpy as np

price = np.array(df["Adj Close"])
percents = (price[1:] - price[:-1])/price[:-1]

percents = df["Adj Close"].pct_change()

#With pct_change() we know the percent change more easy

np.mean(percents)
np.std(percents, ddof = 1)
import matplotlib.pyplot as plp
plp.plot(percents)
plp.ylabel("returns")
plp.xlabel("date")
plp.title("IBM daily retuns")

from statsmodels.stats import weightstats
import scipy.stats
scipy.stats.ttest_1samp(percents, 0, nan_policy = "omit") #The mean of retuns not are differents of zero


weightstats.ztest(percents, alternative = "larger") #We have to reject the hypothesis alternative
input()







