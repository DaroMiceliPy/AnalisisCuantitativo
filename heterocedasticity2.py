from statsmodels.formula.api import ols
import matplotlib.pyplot as plp
import pandas as pd
import numpy as np


dataset = pd.read_excel("heterocedasticity2.xlsx")

formula = "Y~X"
model = ols(formula = formula, data = dataset).fit()

plp.scatter(dataset["X"], dataset["Y"], color = "red", marker="o")
plp.plot(dataset["X"], list(modelo.params)[0] + list(modelo.params)[1]*dataset["X"], color="violet", label="lineregression")
plp.title("model")

#We will to draw the residuals, for to know if the model presents heterocedasticity
plp.scatter(dataset["X"], model.resid)

#The residuals follows a patron, and we can to suspicious about heterocedasticity

usquares = model.resid**2
formula = "y ~ x1"
dataset1 = pd.DataFrame(data = {"y": np.log(usquares), "x1": np.log(dataset["X"])})
model1 = ols(formula = formula, data = dataset1).fit()
model1.summary()

#Seems be that the model not presents heterocedasticity, but, we can to do another proofs, for example, the breush-pagan-godfrey proof

umean = np.mean(modelo.resid**2)
dataset["pi"] = modelo.resid**2/umean
formula = "pi~X"
model2 = ols(formula = formula, data = dataset).fit()
model2.summary() #The x coef is not significative, therefore, the model no presents heterocedasticity

#We have the same conclution if we do the proof white
from statsmodels.stats.diagnostic import het_white
het_white(model1.resid, model1.model.exog)[3]
input()
