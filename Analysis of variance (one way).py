import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
import matplotlib.pyplot as plp
import numpy as np
from scipy import stats
#This example for ANOVA was taken from an example in the book called "Probability and Statistics: Methods and Applications" by George C. Canavos


# we assume that have the following sample representing for list1


list1 = [14.4, 14.8, 15.2, 14.3, 14.6, 14.5, 14.1, 14.6,
             14.2, 13.8, 14.1, 13.7, 13.6, 14, 13, 13.4, 13.2,
             13.1, 12.8, 12.9, 13.2, 13.3, 12.7]

list2 = ["4"] * 5 + ["6"] * 4 + ["8"] * 5 + ["10"] * 3 + ["12"] * 6
data = pd.DataFrame(data={"thickness": list2, "measure": list1
                          })
stats.levene(list(data.loc[data["thickness"] == "4"]["measure"]), list(data.loc[data["thickness"] == "6"]["measure"]), list(data.loc[data["thickness"] == "8"]["measure"]), list(data.loc[data["thickness"] == "10"]["measure"]), list(data.loc[data["thickness"] == "12"]["measure"]))
input()
''' We can see how across the levene test the residuos
have the same variance '''

residuos = list(data.loc[data["thickness"] == "4"]["measure"] - np.mean(data.loc[data["thickness"] == "4"]["measure"])) + list(data.loc[data["thickness"] == "6"]["measure"] - np.mean(data.loc[data["thickness"] == "6"]["measure"])) + list(data.loc[data["thickness"] == "8"]["measure"] - np.mean(data.loc[data["thickness"] == "8"]["measure"])) + list(data.loc[data["thickness"] == "10"]["measure"] - np.mean(data.loc[data["thickness"] == "10"]["measure"])) + list(data.loc[data["thickness"] == "12"]["measure"] - np.mean(data.loc[data["thickness"] == "12"]["measure"]))



''' Preliminarly, we can to draw a boxplot of each thickness.
And if we do a boxplot, it we'll a idea of the tendences central
of the differents treatments
 '''
data.boxplot(column="measure", by="thickness", figsize=(5, 5))
plp.show() #We can see some differences


modelo = ols("measure ~ thickness", data=data).fit()
table = sm.stats.anova_lm(modelo)
print(table)
input()
''' For the hipothesis test, we have a level of significance of 0,01 '''
''' How the p value is most less to 0.01 we have to reject the hypothesis
of the means are equal '''


''' We going to do a plot of normality of residuos '''
residuos = list(data.loc[data["thickness"] == "4"]["measure"] - np.mean(data.loc[data["thickness"] == "4"]["measure"])) + list(data.loc[data["thickness"] == "6"]["measure"] - np.mean(data.loc[data["thickness"] == "6"]["measure"])) + list(data.loc[data["thickness"] == "8"]["measure"] - np.mean(data.loc[data["thickness"] == "8"]["measure"])) + list(data.loc[data["thickness"] == "10"]["measure"] - np.mean(data.loc[data["thickness"] == "10"]["measure"])) + list(data.loc[data["thickness"] == "12"]["measure"] - np.mean(data.loc[data["thickness"] == "12"]["measure"]))
raizCME = np.sqrt(table["mean_sq"][1])
normResid = residuos/raizCME
plp.scatter(x=np.linspace(0, 10, num=23), y=normResid)
plp.axhline(y=0, xmin=0, xmax=23, color="black")
plp.show()


#Another way for to reject the hipothesis null, is the way of
#the statistic critic. The statistic critic is 5,3746, and the 
#statistic empiric is 36.45, therefore, we have to reject the hipothesis null


f = stats.f(4, 18)
linea = np.linspace(f.interval(0.99999)[0], f.interval(0.99999)[1], 1000)
plp.plot(linea, f.pdf(linea), color="black", label="F distribution")
plp.fill_between(np.linspace(f.ppf(0.995), f.ppf(0.99999), 1000), f.pdf(np.linspace(f.ppf(0.995), f.ppf(0.99999), 1000)),color="red", label="Reject the hypothesis")
plp.legend()
plp.show()

'''
Another way for to do ANOVA is using stats from scipy, but, this method is
less clear front the statsmodels method '''

stats.f_oneway([14.4, 14.8, 15.2, 14.3, 14.6], [14.5, 14.1, 14.6,
             14.2], [13.8, 14.1, 13.7, 13.6, 14], [13, 13.4, 13.2],
               [13.1, 12.8, 12.9, 13.2, 13.3, 12.7])
input()


