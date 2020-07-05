'''
Vamos a jugar con un modelo de regresion lineal. Para eso primero vamos a obtener los datos
y luego, vamos a ver si hay una relacion lineal entre x e y. Asi mismo vamos
a probar los supuesto de los MCO. En todos los casos vamos formulas las hipotesis con un
un 5% de significatividad'''


#Vamos a importar las librerias que nos van a servir.
import pandas as pd
import matplotlib.pyplot as plp
import statsmodels.api 
import numpy as np
from scipy import stats

from statsmodels.formula.api import ols
data = pd.DataFrame(data={"y": [4.4567, 5.77, 5.9787, 7.3317, 7.3182, 6.5844, 7.8182, 7.8351, 11.0223, 10.6738, 10.8361, 13.615, 13.531], "x": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]})

formula1 = "y~x" #La fomula es que y depende de x
modelo = ols(formula=formula1, data=data).fit() #Entrenamos el modelo
modelo.summary() #Creamos el reporte con los resultados generales del modelo
''' Por significatividad global vemos que el modelo es bastante bueno (estadistico f). Tambien se prueba 
El supuesto de que los residuos se distribuyen normalmente, ya que el p valor de
la prueba de Jarque-bera no es significativa. Igualmente vamos a realizar un 
histograma de residuos y pasar la curva normal por encima para ver
si la curva se ajusta mas o menos o no a los datos '''

normal = stats.norm(0, 1)
plp.plot(np.linspace(normal.interval(0.999)[0], normal.interval(0.999)[1], num=1000), normal.pdf(np.linspace(normal.interval(0.999)[0], normal.interval(0.999)[1], num=1000)), label="distribucion normal")
plp.hist(modelo.resid, density=1)
plp.legend()
plp.show()

#Vemos que los residuos se distribuyen de manera normal, razonablemente

#Ahora vamos a pasar a hacer el grafico de la regresion

plp.scatter(data["x"], data["y"], marker="o", color="grey", label="observaciones")
plp.plot(data["x"], data["x"]*list(modelo.params)[1] + list(modelo.params)[0], color="black", label="Estimacion")
plp.legend()
plp.show()

#Pasamos a hacer una prueba de homocedasticidad. Esto consiste ver si las varianzas son iguales de los errores son constantes a traves de toda la recta
#Podemos hacer un ploteo de residuos para ver si detectamos algun patron

plp.scatter(data["x"], modelo.resid, color="violet", marker="*", label="residuos")
plp.legend()
plp.show()

#Aparentemente no hay ningun patron entre los valores dados de x y los residuos
#Pero para asegurarnos, podemos hacer el test de white.

''' Lo que hacemos es crear un modelo auxiliar, generando un vector
de los residuos al cuadrado primero. Luego tenemos que modelo el resto del modelo:
    lo que haremos es multiplicar cada variable independiente por si mismas y por las otras variables
    independientes. Como tenemos una sola variable independiente en este modelo de regresion simple vamos
    a tener solo x^2. Luego vemos el test de significatividad global de ese
    modelo para ver si el cambio en las variables exogenas impactan en 
    los errores al cuadrados. Si f es significativo, entonces estamos
    ante la presencia de heterocedasticidad, de los contrario, tenemos homocedasticidad.
    Las hipotesis por lo tanto son
    H0: B1=B2=0
    H1: B1!=B2!=0'''

data["e_cuadrado"] = modelo.resid**2
data["x_cuadrado"] = data["x"]**2
formula2 = "e_cuadrado~x+x_cuadrado"
modelo2 = ols(formula=formula2, data=data).fit()
modelo2.summary()
'''Vemos el test de significatividad y nos arroja que el p valor de del estadistico
es de 0.308, por lo tanto no rechazariamos la hipotesis de homocedasticidad '''

#Pero esto mismo lo podemos hacer con het_white de statsmodels
from statsmodels.stats.diagnostic import het_white
het_white(modelo.resid, modelo.model.exog)[3] #Esta linea nos arroja directamente el p valor del estadistico f
#Podemos ver que es el mismo obtenido por el modelo auxiliar, por lo tanto llevamos a la misma conclusion


''' El otro supuesto del modelo de MCO es de que los errores no estan
autocorrelacionados. Para eso vamos a usar el test de durbin watson,
vamos a obtener el estadistico manualmente y luego lo calculamos con statsmodels
'''
list2 = []
for elemento1, elemento2 in zip(list(modelo.resid)[1:], list(modelo.resid)[0:-1]):
    list2.append((elemento1 - elemento2)**2)
    
EstadisticoDW = sum(list2)/sum(data["e_cuadrado"])
print(str(EstadisticoDW)) #Es el estadistico Durbin-Watson

from statsmodels.stats.stattools import durbin_watson
durbin_watson(modelo.resid) #Obtenemos el mismo estadistico. Pero ahora cual es el criterio de rechazo de que si los
#Errores se autocorrelacionan o no?. Simplle armamos un intervalo.
#Para eso debemos encontrar los limites inferiores y superiores. Vamos a una tabla de durbin_watson y vemos que para
#1 regresora y un tamaño de 13 para la muestra, tenemos: 

''' 0 ----- 0,738 ----- 1,038 ------ 2 ----- 2,962 ----- 3,262 ----- 4. 
Si el estadistico, esta entre 1,038 y 2,962 entonces podemos concluir
que los errores no estan autocorrelacionados. En efecto como el estadistico
esta en ese intervalo, podemos decir que los errores no estan autocorrelacionados '''

#Pero que sucede si los errores estan correlacionados en otros errores anteriores al inmediato error anterior?, la prueba de durbin-watson no responde este problema
#Lo cual una prueba mas general es utilizar la prueba de Breusch Godfrey
#Entonces tendriamos un modelo autorregresivo de la siguiente forma.
# ei = X * B + p1*ei-1 + p2*ei-2 + p3*ei-3 + ... + pm*ei-m + Vi
#Las hipotesis planteadas son las siguientes

# Ho: p1=0, p2=0, p3=0... pm=0
# H1: p1!=0, p2!=0, p3!=0...pm!=0

from statsmodels.stats.diagnostic import acorr_breusch_godfrey
acorr_breusch_godfrey(modelo) #Obtenemos un p valor mayor al 5% por lo tanto podemos concluir que los errores no estan
#Autocorrelacionados

''' Aun asi puede que el modelo no se encuentre bien especificado.
Puede que omitimos una variable e el modelo, puede que no sea una funcion lineal,
por lo tanto, el test que nos permitiria saber eso, es el test de ramsey:
Vamos a crear un modelo auxiliar, en donde tenemos en cuenta que el modelo puede ser especificado en forma polinomica

y = B0 + B1*X1 + B2*y_estimado^2 + u por ejemplo

H0: el modelo esta bien especificado
H1: el modelo no esta bien especificado '''

from statsmodels.stats.diagnostic import linear_reset

linear_reset(modelo, power=2, use_f=True) #Vamos a usar el estadistico f, y un polinomio de grado 2.

#Vemos que el estadistico f es de 3.68 con un p valor de 0,0840 que seria mayor al 0,05 fijado. Por lo tanto podemos concluir que el modelo esta bien especificado


#Ahora que probamos que el modelo en general cumple con los supuestos del modelo de MCO
#Podemos crear por ejemplo unas lineas de intervalo de confianz apara el valor cada valor de y estimado.
#Para ello necesitamos la varianza del modelo

VarModelo = sum(data["e_cuadrado"])/(len(data) - 2)

#Ahora hacemos la varianza para cada valor individual y el intervalo de confianza

data["Variaciones1"] = VarModelo*(1 + 1/len(data) + (data["x"] - np.mean(data["x"]))**2/sum(data["e_cuadrado"]))
data["y_estimado"] = list(modelo.params)[0] + list(modelo.params)[1]*data["x"]
intervaloSuperior1 = data["y_estimado"] + stats.t.ppf(0.975, len(data)) * np.sqrt(data["Variaciones1"])
intervaloInferior1 = data["y_estimado"] - stats.t.ppf(0.975, len(data)) * np.sqrt(data["Variaciones1"])

#Ahora hacemos la varianza para la media, y el intervalo de confianza para la media del y estimado dado un valor de x
data["Variaciones2"] = VarModelo*(1/len(data) + (data["x"] - np.mean(data["x"]))**2/sum(data["e_cuadrado"]))
intervaloSuperior2 = data["y_estimado"] + stats.t.ppf(0.975, len(data)) * np.sqrt(data["Variaciones2"])
intervaloInferior2 = data["y_estimado"] - stats.t.ppf(0.975, len(data)) * np.sqrt(data["Variaciones2"])

fig, ax = plp.subplots(figsize=(6, 6))
plp.scatter(data["x"], data["y"], marker="o", color="grey", label="observaciones")
plp.plot(data["x"], data["x"]*list(modelo.params)[1] + list(modelo.params)[0], color="black", label="Estimacion")
plp.plot(data["x"], intervaloSuperior1, color="red", label="intervalo para la media")
plp.plot(data["x"], intervaloInferior1, color="red")
plp.plot(data["x"], intervaloSuperior2, color="blue", label="intervalo para la prediccion individual")
plp.plot(data["x"], intervaloInferior2, color="blue")
plp.legend()
plp.show()


''' Este ultimo grafico refuerza la idea de introducir nuevos datos
al modelo, ya que a medida que x se aleja de su valor promedio las predicciones
se hacen mas imprecisas '''








