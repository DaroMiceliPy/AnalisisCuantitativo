import numpy as np
import pandas as pd
from statsmodels.formula.api import ols

''' Vamos a realizar experimentos montecarlo, y demostrar las propiedades de insesgadez 
de los estimadores de minimos cuadrados ordinarios '''
''' Supongamos que tenemos la siguiente funcion de regresion poblacional
Y = 20 + 0,6*X , donde B1 = 20 y B2 = 0,6. Escogeremos un tamaño de muestra n = 25,
Los valores de x van a ser desde 1 hasta 25 '''

x1 = np.linspace(1, 25, num=25)



paramsB0 = []
paramsB1 = [] #Aqui estran guardamos los valores de los parametros
 
for i in range(1, 1000):
    u = np.random.randn(25) #Obtenemos 25 numeros aleatorios con distribucion normal
    y = 20 + 0.6*x + u #Encontramos los valores de y simulados
    data = pd.DataFrame(data = {"y": y, "x1": x1})
    modelo = ols(formula = "y~x1", data = data).fit() #Corremos la regresion
    paramsB0.append(modelo.params[0]) #Guardamos el valor del estimador 
    paramsB1.append(modelo.params[1])


np.mean(paramsB0) #Calculamos el promedio de los estimadores del estimador
np.mean(paramsB1)

''' Como la media de los parametros estimados son muy cercanos a los verdaderos
parametros poblacionales, podemos decir que los estimadores cumplen con la propiedad de insesgadez '''






