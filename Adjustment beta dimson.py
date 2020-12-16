import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import pandas_datareader as GetData

MSFT = GetData.get_data_yahoo("MSFT", start = "2020-1-1", end = "2020-8-8")
SP500 = GetData.get_data_yahoo("^GSPC", start = "2020-1-1", end = "2020-8-8")

MSFT["RT"] = MSFT["Adj Close"].pct_change()

SP500["RTMKT"] = SP500["Adj Close"].pct_change()
SP500["RTLAG"] = SP500["RTMKT"].shift(1)
SP500["RTLEAD"] = SP500["RTMKT"].shift(-1)

newdata = pd.merge(SP500, MSFT, on = "Date")

formula = "RT ~ RTMKT + RTLAG + RTLEAD"

model = ols(formula = formula, data = newdata).fit()
model.summary()

''' Therefore the beta adjustment is... '''
betaAdj = model.params[1] + model.params[2] + model.params[3]
betaAdj
input()

