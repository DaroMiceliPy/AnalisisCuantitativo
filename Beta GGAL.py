import pandas_datareader as pdr
from scipy import stats
import matplotlib.pyplot as plp
start = "2010-1-1"
end = "2020-6-5"
retGGAL = pdr.get_data_yahoo("GGAL", start = start, end = end)["Adj Close"].pct_change().dropna()
#En una sola linea descargamos los valores al cierre de una fecha de inicio a otra de final
#Calculamos los rendimientos diarios con pct_change() y luego eliminamos los valores faltantes como NaN con dropna()
retSP500 = pdr.get_data_yahoo("^GSPC", start = start, end = end)["Adj Close"].pct_change().dropna()
#Lo mismo hacemos con el SP500

regresion = stats.linregress(retSP500, retGGAL)
print("El cambio de la rentabilidad de la accion GGAL con respecto al indice SP500 es igual a:\n" + str(regresion.slope))
help(stats.linregress)

plp.scatter(retSP500, retGGAL)
plp.plot(retSP500, regresion.slope*retSP500 + regresion.intercept, color="r")
plp.title("Regresion Beta")
plp.ylabel("GGAL")
plp.xlabel("SP500")
plp.show()
