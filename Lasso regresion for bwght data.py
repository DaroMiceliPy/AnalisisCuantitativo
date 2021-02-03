import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plp
import seaborn as sns



data = pd.read_csv("C:\\Users\\darioylauri\\Desktop\\data_bwght2.csv")
data = data.dropna() #Eliminamos valores nulos
sns.heatmap(data.corr(), square = True) #Creamos la matriz de correlacion


data2 = data.drop(["bwght", "lbwght", "Unnamed: 0", "lbw", "vlbw"], axis = 1)

X_matrix = data2.to_numpy()

Y_matrix = np.array(data["bwght"]).reshape(len(data), 1)

X_train, X_test, Y_train, Y_test = train_test_split(X_matrix, Y_matrix, train_size = 0.5)

model = linear_model.LinearRegression()

model.fit(X_train, Y_train)

model.score(X_train, Y_train)
model.score(X_test, Y_test)

plp.bar(np.arange(len(model.coef_[0])), list(model.coef_[0]))

model2 = linear_model.Lasso(alpha = 1.0)

model2.fit(X_train, Y_train)

model2.score(X_train, Y_train)
model2.score(X_test, Y_test)

plp.bar(np.arange(len(model2.coef_)), model2.coef_)

#We need to obtain the optimal alpha value for LASSO
model3 = linear_model.LassoCV()
model3.fit(X_train, Y_train)
model3.alpha_

model3.score(X_train, Y_train)
model3.score(X_test, Y_test)

num = 0
for i in list(model3.coef_):
    if i != 0:
        num = num + 1

plp.bar(np.arange(len(model3.coef_)), list(model3.coef_))

regressors = pd.DataFrame(data = {"Explanatory variables": list(data2.columns), "Values for LASSO": list(model3.coef_)})

print("The numbers of explanatory variables chosen in the model are: " + str(num))


