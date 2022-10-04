consumo.loc[consumo['dia_semana'].isin(['Tuesday','Friday'])].groupby('dia_semana')['consumo_kwh','precio_kwh'].mean()

index = [a or b for a,b in zip(consumo["dia_semana"]=="Tuesday",consumo["dia_semana"]=="Friday")]
consumo_y_precio_groupby = consumo[index].groupby("dia_semana")[["consumo_kwh", "precio_kwh"]].mean()