
from xml.etree.ElementInclude import include
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

datos = pd.read_csv("C:/Users/alber/OneDrive/Documentos/GitHub/BigDataConPython/Competiciones kaggle/House prices/train.csv", sep=",", header=0)

datos = datos[["1stFlrSF" , "SalePrice"]]
#Cambio el nombre de la columna
datos = datos.rename(columns={"1stFlrSF" : "FirstFlrSF"})
print(datos.head( ))
print(datos.info())

sns.scatterplot(x="FirstFlrSF", y="SalePrice", data=datos)
plt.show()
#Creo un modelo
modelo = smf.ols("SalePrice ~ FirstFlrSF", data=datos).fit()
print(modelo.summary().tables[1])

