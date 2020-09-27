import pandas as pd
from statsmodels.formula.api import ols

dataset = pd.read_excel("Table 9_1.xlsx")
#Where D2 has value 1 when is on the northeast or nort-center, and has value 0 elsewhere
#And D3 has value 1 when the state is on the Sur, and has value 0 elsewhere


modelo = ols("Salary ~ C(D2) + C(D3)", data = dataset).fit() #With c(), we indicates the cathegorical variable
modelo.summary()

#How the p values of the coefficients, are less significative, we conclude, that there are not differences between zones

