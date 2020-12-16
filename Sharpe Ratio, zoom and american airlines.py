import pandas as pd
from scipy import stats
import pandas_datareader as GetData
import numpy as np
from statsmodels.formula.api import ols

FVX = GetData.get_data_yahoo("^FVX", start = "2019-12-1", end = "2020-12-1")
ZM = GetData.get_data_yahoo("ZM", start = "2019-12-1", end = "2020-12-1")
AAL = GetData.get_data_yahoo("AAL", start = "2019-12-1", end = "2020-12-1")

stats.shapiro(FVX["Adj Close"].pct_change()[1:])
stats.shapiro(ZM["Adj Close"].pct_change()[1:])

num1 = ZM["Adj Close"].pct_change() - FVX["Adj Close"].pct_change()
Sharpe1 = np.mean(num1)/np.std(num1, ddof = 1)
num2 = AAL["Adj Close"].pct_change() - FVX["Adj Close"].pct_change()
Sharpe2 = np.mean(num2)/np.std(num2, ddof = 1)
print(Sharpe1)
print(Sharpe2)


''' Although the returns stocks are ot distributed normally,
we can see how useful, is the analyze ex-ports of stocks. In this case
of two stocks: zoom and American Airlines '''
