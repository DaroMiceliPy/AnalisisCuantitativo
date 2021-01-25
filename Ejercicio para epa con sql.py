import sqlite3
import sklearn as sk
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plp

coneccion = sqlite3.connect("C:\\Users\\darioylauri\\Desktop\\SQL_coursera.db")
cursor = coneccion.cursor()
cursor.execute("CREATE TABLE EJERCICIO_EPA (cantidad_gastada_en_alimentos integer, tamaño_familia integer)")

cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (99, 3)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (104, 6)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (151, 5)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (129, 6)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (142, 6)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (111, 3)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (74, 4)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (91, 4)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (119, 5)")
cursor.execute("INSERT INTO EJERCICIO_EPA VALUES (91, 3)")

coneccion.commit()


data = pd.read_sql("SELECT * FROM EJERCICIO_EPA", coneccion)
X = np.array(data["tamaño_familia"]).reshape(len(data),1)
y = np.array(data["cantidad_gastada_en_alimentos"]).reshape(len(data), 1)
regresion = linear_model.LinearRegression()
regresion.fit(X, y)
regresion.intercept_
regresion.coef_
regresion.predict(np.array([[4]])) #Prediction

r2_score(regresion.predict(X), y)

plp.scatter(data["tamaño_familia"], data["cantidad_gastada_en_alimentos"], label = "datos reales")
plp.plot(X, regresion.predict(X), linewidth = 3, color = "yellow", label = "prediccion")
plp.xlabel("tamaño de la familia")
plp.ylabel("cantidad gastada en alimentos")
plp.show()
