import pandas_datareader as GetData
import datetime
import scipy.stats
import numpy as np




def ret(ticker,BegData,EndData):
    p = GetData.get_data_yahoo(ticker, BegData, EndData)
    return(p["Adj Close"].pct_change())

IBM = ret("IBM", "2019-9-18", "2020-9-18")
MSFT = ret("MSFT", "2019-9-18", "2020-9-18")


if np.var(IBM, ddof = 1) >= np.var(MSFT, ddof = 1):
    pvalue = scipy.stats.f.sf(np.var(IBM, ddof = 1)/np.var(MSFT, ddof = 1), len(IBM) - 1, len(MSFT) - 1)
    print(pvalue)
else:
    pvalue = scipy.stats.f.sf(np.var(MSFT, ddof = 1)/np.var(IBM, ddof = 1), len(MSFT) - 1, len(IBM) - 1)
    print(pvalue)


    
#How the pvalue is 0.093, we can see that the variance are equals
#But if we need to compare more than two variance, we need to use the barlett test
GGAL = ret("GGAL", "2019-9-18", "2020-9-18")
scipy.stats.bartlett(IBM, MSFT, GGAL) #The p value suggests that the two variance are differents

#The assumption for bartlett test is that the stock returns follow a normal distribution



