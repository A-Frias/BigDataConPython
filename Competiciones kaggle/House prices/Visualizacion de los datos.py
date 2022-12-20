import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

datos = pd.read_csv("C:/Users/alber/OneDrive/Documentos/GitHub/BigDataConPython/Competiciones kaggle/House prices/train.csv", sep=",", header=0)
#muestro todas las columnas
pd.set_option('display.max_columns', None)
print(datos.head( ))
#print(datos.describe())
print(datos.info())
#escribo el numero de columnas
#datos_continuos = datos.select_dtypes(include=['int64', 'float64'])
#datos_discretos = datos.select_dtypes(include=['object'])

#Cambio los nombres de las columnas para que no empiecen por numero
datos = datos.rename(columns={"1stFlrSF" : "FirstFlrSF", "2ndFlrSF" : "SecondFlrSF", "3SsnPorch" : "ThreeSsnPorch"})


datos_relevantes=pd.DataFrame({"SalePrice" : list(datos["SalePrice"])})
#Creo un modelo de regresion lineal para cada variable y muestro sus coeficientes y su p-value
for i in datos.columns:
    #print(i)
    if i != "SalePrice":
        tmp = pd.DataFrame({i : list(datos[i])}).dropna()
        modelo = smf.ols("SalePrice ~ " + i, data=datos).fit()
        #muestro el nombre de la variable
        
        #print(modelo.pvalues[:])
        #muestro en pantalla unicamnete los coeficientes y el p-value de cada variable
        #print(modelo.summary().tables[1])
        #print(" ")

        #Creo un nuevo dataframe con las variables con p-value menor a 0.05
        tmp = modelo.pvalues[:]

        
        if len(tmp)>2:
            if tmp.drop(tmp.drop(tmp.idxmin()).idxmin()).min() < 0.05:
                datos_relevantes[i]=datos[i]
            else:
                pass
        else:    
            if tmp.drop(tmp.idxmin()).min() < 0.05:
                datos_relevantes[i]=datos[i]
            else:
                pass
    else:
        pass   
#print(datos_relevantes.head())
#
#print(len(datos_relevantes.columns))
#
##Creo una matriz de correlacion
#corr = datos_relevantes.corr()
#print(corr)
#
datos_relevantes = datos_relevantes.drop(columns=["PoolQC"])
#Creo un modelo de regresion lineak con todas las variables
primer_cuarto = datos_relevantes.columns[1:17]
segundo_cuarto = datos_relevantes.columns[17:33]
tercer_cuarto = datos_relevantes.columns[33:49]
cuarto_cuarto = datos_relevantes.columns[49: ]
formula1="SalePrice ~ " + " + ".join(primer_cuarto[:])
formula2="SalePrice ~ " + " + ".join(segundo_cuarto[:])
formula3="SalePrice ~ " + " + ".join(tercer_cuarto[:])
formula4="SalePrice ~ " + " + ".join(cuarto_cuarto[:])

datos1 = datos_relevantes[primer_cuarto]
datos2 = datos_relevantes[segundo_cuarto]
datos3 = datos_relevantes[tercer_cuarto]
datos4 = datos_relevantes[cuarto_cuarto]

print(datos4.info())

modelo1 = smf.ols(formula1 , data=datos_relevantes).fit()
print(modelo1.summary())
modelo2 = smf.ols(formula2 , data=datos_relevantes).fit()
print(modelo2.summary())
modelo3 = smf.ols(formula3 , data=datos_relevantes).fit()
print(modelo3.summary())
modelo4 = smf.ols(formula4 , data=datos_relevantes).fit()
print(modelo4.summary())


variables_interesantes = ["RoofMatl", "Exterior1st", "MasVnrType", "ExterQual", "BsmtQual", "BsmtExposure", "BsmtFinType1", 
                        "YearBuilt", "YearRemodAdd ", "MasVnrArea", "BsmtFinSF1", "BsmtFinType2", "HeatingQC", "CentralAir", "Electrical", "KitchenQual",
                        "Functional", "BsmtUnfSF", "TotalBsmtSF", "Heating", "FirstFlrSF", "SecndFlrSF",  "BsmtFullBath", "FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr"]

primera_criba = pd.concat([datos_relevantes["SalePrice"], datos[primer_cuarto] ,datos[variables_interesantes] , datos
[cuarto_cuarto] ], axis=1)
print(primera_criba)