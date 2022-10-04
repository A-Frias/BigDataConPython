import os
from turtle import shape
import numpy as np
import pandas as pd

os.chdir("C:/Users/alber/OneDrive/Documentos/GitHub/BigDataConPython/Master BD Python/5.2 Librerias para ciencia de datos/Ejercicios")
#importamos la tabla de datos consumo_horario_cliente.csv
consumo = pd.read_csv("consumo_horario_cliente.csv", sep=";")
#print(consumo.head())
consumo["datetime"] = pd.to_datetime(consumo["datetime"])
consumo_h5 = consumo.head(5)
#consumo_h5["datetime"] = 
#print(consumo_h5["datetime"].dt.date)
#print(consumo_h5["datetime"].dt.time)
#print(consumo_h5["datetime"].dt.year)
#print(consumo_h5["datetime"].dt.month)
#print(consumo_h5["datetime"].dt.day)
#print(consumo_h5["datetime"].dt.hour)
#print(consumo_h5["datetime"].dt.day_name())

consumo = consumo.assign(
    coste_eur = consumo["consumo_kwh"] * consumo["precio_kwh"],
    dia_semana = consumo["datetime"].dt.day_name(),
    fecha = consumo["datetime"].dt.date,
    hora = consumo["datetime"].dt.hour,
    #hora2 = consumo["datetime"].dt.time,
    mes = consumo["datetime"].dt.month
)
#print(consumo.head())


consumo_maximo = consumo["consumo_kwh"].max()
#print(consumo_maximo)
dia_consumo_maximo = consumo[consumo["consumo_kwh"] == consumo_maximo][["consumo_kwh", "fecha", "hora"]]
#print(dia_consumo_maximo)

horas_poco_consumo = consumo[consumo["consumo_kwh"]< 0.02][["fecha", "hora"]]
#print(horas_poco_consumo)

consumo_premedio_martes = consumo[consumo["dia_semana"]=="Tuesday"]["consumo_kwh"].mean()
#print(consumo_premedio_martes)

precio_promedio_kwh = consumo["precio_kwh"].mean()

#index = consumo["dia_semana"]=="Tuesday" or consumo["dia_semana"]=="Friday"
index = [a or b for a,b in zip(consumo["dia_semana"]=="Tuesday",consumo["dia_semana"]=="Friday")]

consumo_y_precio_M_y_V = consumo[(consumo["dia_semana"]=="Tuesday")|(consumo["dia_semana"]=="Friday")][["consumo_kwh", "precio_kwh"]].mean()
print(consumo_y_precio_M_y_V)

consumo_y_precio_groupby = consumo[(consumo["dia_semana"]=="Tuesday")|(consumo["dia_semana"]=="Friday")].groupby("dia_semana")[["consumo_kwh", "precio_kwh"]].mean()
print(consumo_y_precio_groupby)

#print(consumo.loc[consumo['dia_semana'].isin(['Tuesday','Friday'])].groupby('dia_semana')['consumo_kwh','precio_kwh'].mean())

consumo_y_precio_por_mes = consumo.groupby("mes")[["consumo_kwh","precio_kwh"]].mean()
#print(consumo_y_precio_por_mes)



precio_md= pd.read_csv("C:/Users/alber/OneDrive/Documentos/GitHub/BigDataConPython/Master BD Python/5.2 Librerias para ciencia de datos/Ejercicios/precio_md.csv" , sep=";")
#print(precio_md.head())
precio_md["datetime"] = pd.to_datetime(precio_md["datetime"])
precio_md = precio_md.assign(
            fecha = precio_md["datetime"].dt.date,
            hora = precio_md ["datetime"].dt.hour
)

precio_md.index = precio_md[["fecha","hora"]]
consumo.index = consumo[["fecha","hora"]]
precio_md = precio_md.drop(columns=["datetime","fecha","hora"])
consumo = consumo.drop(columns=["datetime","fecha","hora"])

#precio_md.join(consumo_md, on=["fecha","hora"], how="inner")

consumo_md = pd.merge(consumo, precio_md, how="inner", left_index=True, right_index=True)
print(consumo_md.iloc[consumo_md.isna().any(axis=1).values])
consumo_md["preciomd_eurMw"] = consumo_md["preciomd_eurMw"]/1000
consumo_md.rename(columns={"preciomd_eurMw":"precio_md_kwh"}, inplace=True)

#print(consumo_md.head())

consumo_md = consumo_md.assign(diff_precio = consumo_md["precio_kwh"] - consumo_md["precio_md_kwh"])

print(consumo_md.groupby("mes")["diff_precio"].mean())
