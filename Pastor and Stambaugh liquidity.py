import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import pandas_datareader as GetData
import pandas_datareader.data as reader

''' Pastor and stambaugh liquidity measure '''

MELI = GetData.get_data_yahoo("IBM", start = "2013-1-1", end = "2013-1-31")
SP500 = GetData.get_data_yahoo("^GSPC", start = "2013-1-1", end = "2013-1-31")
IRX = GetData.get_data_yahoo("^IRX", start = "2013-1-1", end = "2013-1-31")

MELI["retMELI"] = MELI["Adj Close"].pct_change()
SP500["retSP500"] = SP500["Adj Close"].pct_change()

newdata = pd.merge(MELI, SP500, on = "Date")
newdata["IRX"] = IRX["Adj Close"].pct_change()

newdata["dollar"] = newdata["Adj Close_x"]*newdata["Volume_x"]
newdata["X2"] = np.sign(newdata["retMELI"] - newdata["IRX"])*newdata["Adj Close_x"]*newdata["Volume_x"]
newdata["X1"] = newdata["retSP500"].shift(-1)
newdata["X2"] = newdata["X2"].shift(-1)

newdata["y"] = newdata["retMELI"] - newdata["retSP500"]

formula = "y ~ X1 + X2"
model = ols(formula = formula, data = newdata).fit()
model.summary()

