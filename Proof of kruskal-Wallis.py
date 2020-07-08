''' Let's go to do a proof non parametric, tall "kruskal-Wallis".
I going to show how to aplicate this proof in python, and how to graphic the
statistic 

We suports that we have the next data about the sales of diferents stablishment of a enterprise.

Sucursal A Sucursal B Sucursal C
11          17          12
7           2           18
3           8           13
4          14            9
10         5            15
6          1            16

And we need to know if there are differences in a the mean of the sales for each stablihsment
'''

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plp

data = pd.DataFrame(data={"Stablishment A": [11, 7, 3, 4, 10, 6], "Stablishment B":
                          [17, 2, 8, 14, 5, 1], "Stablishment C": [12, 18, 13, 9, 15, 16]})
result = stats.kruskal(data["Stablishment A"], data["Stablishment B"], data["Stablishment C"])
print("The statistic obtained is: " + str(result[0]) + " and the pvalue is:" + str(result[1]))

x = stats.chi2(len(list(data.columns)) - 1)
intervalo = np.linspace(x.interval(0.99)[0], x.interval(0.99)[1], 1000)
lineallena = np.linspace(x.ppf(0.0049), x.ppf(0.95), 1000)
zoneReject = np.linspace(x.ppf(0.95), max(intervalo), 1000)
fig, ax = plp.subplots(figsize=(8, 6))
plp.plot(intervalo, x.pdf(intervalo), label="Chi-square distribution", color="black")
plp.fill_between(lineallena, x.pdf(lineallena), label="Zone of acept hypothesis null")
plp.fill_between(zoneReject, x.pdf(zoneReject), label="Zone of Reject the hipothesys null", color="red")
plp.legend()

print("We can see, how clearly the statistic empiric is to the right of the value critic. ")
print("And then, we must to reject the hipothesys ")
input()
