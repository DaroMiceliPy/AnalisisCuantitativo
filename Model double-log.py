import pandas as pd
from statsmodels.formula.api import ols
from numpy import log as ln
''' This is an example of how to applicate the cobb-douglas function of production '''
dataset = pd.read_excel("https://www2.census.gov/programs-surveys/asm/data/2016/ASM_2016_31AS102_with_ann.xlsx")
dataset = dataset.loc[dataset["Year"] == 2016] #We obtein the dates of 2016 year
dataset = dataset[["Geographic area name", "Total cost of materials ($1,000)","Cost of contract work ($1,000)", "Total capital expenditures ($1,000)"]]
y = ln(dataset["Total cost of materials ($1,000)"][0:102]) #We applicate the logarithm
x1 = ln(dataset["Cost of contract work ($1,000)"][0:102])
x2 = ln(dataset["Total capital expenditures ($1,000)"][0:102])
dataset = pd.DataFrame(data = {"y": y, "x1": x1, "x2": x2})

formula = "y~x1+x2"
''' thus, the model is ln(yt) = b0 + b1*ln(x1) + b2*ln(x2) '''
modelo = ols(formula=formula, data=dataset).fit()
print(modelo.summary())

'''We can see how the model is good since R-squared, though, the x1 variable is less significative...
The variable x2 is most significative, if we sum the  B1 + B2.. 0.9995 + 0.0116 = 1.011 we obtein increasing returns to scale. 
The capital is most important for to explain the producttion'''

input()




