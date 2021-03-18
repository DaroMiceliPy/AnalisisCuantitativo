# -*- coding: utf-8 -*-
"""Naive bayes en sklearn con iris dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1StJpP11v7SAIcc0TTMJyZzvdWdYkai2u
"""

import pandas as pd
import matplotlib.pyplot as plp
import numpy as np
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
''' Ahora vamos construir un modelo de clasificacion que nos permita predecir 
a que especie pertenece cada flor dependiendo de sus caracteristicas, como los petalos y demas '''


iris = sbn.load_dataset("iris")

iris.info()
iris

sbn.pairplot(iris, hue = "species") #Con este tipo de grafico vemos las relaciones entre las distintas variables

X = iris.drop(["species"], axis = 1).to_numpy()
Y = iris["species"].to_numpy() #De esta manera generamos las dos matrices para que sklearn pueda trabajar con ellas

X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size = 0.33) #Se paramos los datasets en entrenamiento y prueba

model = GaussianNB()
model.fit(X_train, Y_train)

y_pred = model.predict(x_test)

accuracy_score(y_test, y_pred) #Aca finalmente vemos cual es el accuracy del modelo, vemos que naive bayes funciona bien para este dataset