import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from statsmodels.api import formula
from statsmodels.formula.api import ols


    
hprice2 = pd.read_csv("C:\\Users\\darioylauri\\Desktop\\hprice2.csv")
hprice2.columns #Miramos los nombres de las columnas
hprice2 = hprice2.drop(["Unnamed: 0", "lprice", "lnox", "lproptax"], axis = 1) #Eliminamos las columnas que no usaremos
hprice2.dtypes #Vemos los tipos de datos del data frame

formula = "price~crime+nox+rooms+dist+radial+proptax+stratio+lowstat"
model1 = ols(formula, hprice2).fit()
model1.summary()


X_matrix = hprice2.drop(["price"], axis = 1).to_numpy()
Y_matrix = hprice2["price"].to_numpy().reshape(len(hprice2), 1)

X_train, X_test, Y_train, Y_test = train_test_split(X_matrix, Y_matrix, train_size = 0.7)

model2 = linear_model.LinearRegression()
model2.fit(X_train, Y_train)


mean_squared_error(Y_train, model2.predict(X_train))
mean_squared_error(Y_test, model2.predict(X_test))
model2.score(X_train, Y_train)
model2.score(X_test, Y_test)

''' Como el error cuadratico medio del testeo es muy cercano al error cuadratico
medio del modelo del entrenamiento, asi como tambien el R^2, podemos quedarnos con el modelo original '''

''' Entonces el modelo para la produccion es model1 '''



