import numpy as np
import matplotlib.pyplot as plp
import pandas_datareader as reader
from scipy import stats

def download(ticker, beg, end):
    data = reader.get_data_yahoo(ticker, beg, end)
    return(data["Adj Close"].pct_change())
    

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
         2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

betas = []
for i in range(0, len(years) - 2):
    UL = download("UL", years[i], years[i+1])
    SYP = download("^GSPC", years[i], years[i+1])
    regression = stats.linregress(SYP[1:], UL[1:])
    betas.append(regression.slope)
    
plp.plot(years[1:-1], betas)
plp.xlabel("years")
plp.ylabel("betas coefficients")
plp.title("Moving Beta")
plp.show()

    



