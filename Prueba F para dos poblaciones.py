from scipy import stats
import pandas_datareader as pdr
import numpy as np

#Queremos saber si la varianza de los rendimientos es diferente en ambas acciones, con un alfa del 5%
BRIO = pdr.get_data_yahoo("BRIO.BA", start="2020-1-1", end="2020-5-1")["Adj Close"] #Nos da las cotizaciones al cierre de las acciones del banco santander rio
#Desde el 1 de mayo del 2000 al 1 de mayo del 2020 

GGAL = pdr.get_data_yahoo("GGAL.BA", start="2020-1-1", end="2020-5-1")["Adj Close"] #Hacemos lo mismo con GGAL
#Pero nos interesa los rendimientos, asi que debemos hacer operaciones para sacar el rendimiento diario

ListaRendimientosBRIO = [0]
ListaRendimientosGGAL = [0]
len(GGAL)
for i in range(1, len(BRIO) - 1):
    ListaRendimientosBRIO.append((BRIO[i]/BRIO[i - 1]) - 1)
    ListaRendimientosGGAL.append((GGAL[i]/GGAL[i - 1]) - 1)

stats.f.cdf(np.var(ListaRendimientosGGAL, ddof=1)/np.var(ListaRendimientosBRIO, ddof=1), len(BRIO) - 1, len(GGAL) - 1)
print("Vamos a establecer los intervalos de confianza de las dos varianzas")
CocienteVar = np.var(ListaRendimientosGGAL, ddof=1)/np.var(ListaRendimientosBRIO, ddof=1)
Intervalos = [stats.f.ppf(0.025, len(GGAL) - 1, len(BRIO) - 1)*CocienteVar, stats.f.ppf(0.975, len(GGAL) - 1, len(BRIO) - 1)*CocienteVar]
if Intervalos[0] < 1 and 1 < Intervalos[1]:
    print("El intervalo de cofianza es de: " + str(Intervalos) + "Por lo tanto concluimos que las varianzas con iguales")
    print("Osea no hay diferencia en la variabilidad de los rendimientos de las acciones")
else:
    print("Como el intervalo de confianza: "+ str(Intervalos) + " No contiene al 1 podemos decir que las varianzas de los rendimientos no son iguales")
    




