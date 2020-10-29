from statsmodels.formula.api import ols
import matplotlib.pyplot as plp
import pandas as pd
import numpy as np

data = pd.read_excel("heterocedasticity1.xlsx")
formula = "Y~X"

modelo = ols(formula = formula, data = data).fit()
modelo.summary()

#And now, we will to show if the model presents heterocedasticity

plp.scatter(data["X"], data["Y"], marker="o", color="green", label="residuos")
plp.plot(data["X"], list(modelo.params)[0] + list(modelo.params)[1]*data["X"], label="linea de regresion")
plp.title("modelo")
#Seems be, that the model presents heterocedasticity for the extreme aberrant data
#We can prove that

plp.scatter(data["X"], modelo.resid, marker="o", color="grey")

#But if we want to be more formally, we need to do proofs..
#That we will do name "proof of park"
usquares = modelo.resid**2
#We going to create a new Data Frame
dataset1 = pd.DataFrame(data = {"y": np.log(usquares), "x": np.log(data["X"])})

formula = "y~x"
modelo = ols(formula = formula, data = dataset1).fit()
modelo.summary()

input()

#How the param B1 is not significative, we conclude that the model not presents heteroscedasticity
