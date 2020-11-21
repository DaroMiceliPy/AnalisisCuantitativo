import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
import pandas_datareader.data as reader
import datetime as dt
from scipy import stats

#Creamos los objetos date
start = dt.date(2010, 1, 1)
end = dt.date(2019, 12, 31)

#Descargamos el rendimientos de los retornos de la accion de apple 
yahoo = reader.get_data_yahoo("AAPL", start = start, end = end)["Adj Close"].pct_change()

#Descargamos los 3 factores de fama-french para poder correr la regresion
factors = reader.DataReader("F-F_Research_Data_Factors", "famafrench", start = start, end = end)
factors = factors[0]
#Pasamos de retornos diarios a retornos mensuales
yahoo = yahoo.resample("M").sum()

#Unificamos ambos indices de los dataframes para poder juntarlos.
yahoo.index = factors.index

dataset = pd.merge(yahoo, factors, on = "Date")
dataset["Mkt"] = dataset["Mkt-RF"]/100
dataset["SMB"] = dataset["SMB"]/100
dataset["HML"] = dataset["HML"]/100
dataset["RF"] = dataset["RF"]/100
dataset["AAPL"] = dataset["Adj Close"] - dataset["RF"]
dataset
dataset = dataset.drop(["Adj Close"], axis=1)
dataset

#Entrenamos el modelo
formula = "AAPL ~ Mkt+SMB+HML"
modelo = ols(formula = formula, data = dataset).fit()
modelo.summary()
#Guardamos el valor del R^2 en la variable Rnew
Rnew = 0.301

#Corremos el modelo del CAMP
formula = "AAPL ~ Mkt"
modelo = ols(formula = formula, data = dataset).fit()
modelo.summary()

#Guardamos el valor del R^2 del camp en la variable Rold
Rold = 0.248

#Realizamos el test para saber si formalmente conviene introducir las variables
#Al modelo del CAMP-
F = ((Rnew - Rold)/2)/((1 - Rnew)/116)
Dist = stats.f(2, 116)
Dist.sf(F)

#Calculamos los valores del sistema de ecuaciones normales de Gauss
n = len(dataset)
Mkt = sum(dataset["Mkt"])
SMB = sum(dataset["SMB"])
HML = sum(dataset["HML"])
AAPL = sum(dataset["AAPL"])
#Segundo renglon
Mktcuadrado = sum(dataset["Mkt"]**2)
MktporSMB = sum(dataset["Mkt"]*dataset["SMB"])
MktporHML = sum(dataset["Mkt"]*dataset["HML"])
MktporAAPL = sum(dataset["Mkt"]*dataset["AAPL"])
#Tercer renglon
SMBcuadrado = sum(dataset["SMB"]**2)
SMBporHML = sum(dataset["SMB"]*dataset["HML"])
SMBporAAPL = sum(dataset["SMB"]*dataset["AAPL"])
#Cuarto renglon
HMLcuadrado = sum(dataset["HML"]**2)
HMLporAAPL = sum(dataset["HML"]*dataset["AAPL"])


a = np.array([[n, Mkt, SMB, HML],
              [Mkt, Mktcuadrado, MktporSMB, MktporHML],
              [SMB, MktporSMB, SMBcuadrado, SMBporHML],
              [HML, MktporHML, SMBporHML, HMLcuadrado]])

b = np.array([AAPL, MktporAAPL, SMBporAAPL, HMLporAAPL])
#Resolvemos el sistema.
np.linalg.solve(a, b)



