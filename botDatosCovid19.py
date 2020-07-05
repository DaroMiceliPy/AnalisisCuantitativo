import os
import numpy as np
import matplotlib.pyplot as plp
import requests
import pandas as pd
import datetime
from scipy import stats

DestinoArchivo = os.getcwd() + '\\Data.xlsx' #Creamos el directorio donde se guardara el archivo
url = 'https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.xlsx?raw=true'
archivo = requests.get(url)

open(DestinoArchivo, 'wb').write(archivo.content)

os.chdir(os.getcwd())

covid = pd.read_excel("Data.xlsx") #Accedemos al archivo creado mediante pandas
Argentina = covid.loc[covid["location"] == "Argentina"] #indicamos que queremos filtrar en el data frame los numeros de argentina
hoy = str(datetime.date.today())
ayer = str(datetime.date.today() - datetime.timedelta(days=1))

covid["Letalidad"] = covid["total_deaths"]/covid["total_cases"] #Creamos una nueva columna en el data frame

if len(list(covid.loc[covid["date"] == hoy].index)) == 0: #Lo que hace esta linea es ver si el archivo tiene los datos actualizados al dia de hoy y de lo contrario ejecuta la condicion de abajo
    covidAyer = covid.loc[covid["date"] == ayer]
    media = np.mean(covidAyer["Letalidad"])
    Intervalo = str(list(stats.bayes_mvs(covidAyer["Letalidad"], alpha=0.95))[0][1]) #Con ayuda de esta linea calculamos el intervalo de confianza de la tasa de letalidad
    world = covid.loc[covid["location"] == "World"]
    worldAyer = world.loc[world["date"] == ayer]
    NewworldDeath = worldAyer["total_deaths"]
    NewworldCases = worldAyer["total_cases"]
    Newworldnewcases = worldAyer["new_cases"]
    TOTAL_DEATHS = np.array(NewworldDeath.array)[0]
    TOTAL_CASES = np.array(NewworldCases.array)[0]
    TOTAL_NEWCASES = np.array(Newworldnewcases.array)[0]
    print("El promedio de la tasa de letalidad mundial es de: " + str(media))
    print("El intervalo de confianza de la tasa de letalidad con una confianza del 95% es: " + str(Intervalo))
    print("Las muertes totales hasta hoy es: " + str(TOTAL_DEATHS))
    print("El total de infectados hasta ahora es de: " + str(TOTAL_CASES))
    print("Los nuevos casos registrados hoy es de: " + str(TOTAL_NEWCASES))
    
    
elif len(list(covid.loc[covid["date"] == hoy].index)) != 0:
    covidHoy = covid.loc[covid["date"] == hoy]
    media = np.mean(covidHoy["Letalidad"])
    Intervalo = str(list(stats.bayes_mvs(covidHoy["Letalidad"])[0][1]))
    world = covid.loc[covid["location"] == "World"]
    worldHoy = world.loc[world["date"] == hoy]
    NewworldDeath = worldHoy["total_deaths"]
    NewworldCases = worldHoy["total_cases"]
    Newworldnewcases = worldHoy["new_cases"]
    TOTAL_DEATHS = np.array(NewworldDeath.array)[0]
    TOTAL_CASES = np.array(NewworldCases.array)[0]
    TOTAL_NEWCASES = np.array(Newworldnewcases.array)[0]
    print("El promedio de la tasa de letalidad mundial es de: " + str(media))
    print("El intervalo de confianza de la tasa de letalidad con una confianza del 95% es: " + str(Intervalo))
    print("Las muertes totales hasta hoy es: " + str(TOTAL_DEATHS))
    print("El total de infectados hasta ahora es de: " + str(TOTAL_CASES))
    print("Los nuevos casos registrados hoy es de: " + str(TOTAL_NEWCASES))

#Con estas lineas graficamos la curva de infectados.
plp.plot(Argentina["total_cases"])
plp.title("Evolucion del coronavirus en Argentina")
plp.ylabel("Infectados")
plp.show()

input()

os.remove("Data.xlsx")

