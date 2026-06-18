import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#el filtro avanzado va buscando los filtros 
#sobre el total de registros registrados en la columna de harwaretype 
#ante la columnas con esa misma inicial de nombre siendo avance
#luego buscara la suma total del filtro sobre la tabla trade
#en donde nos mostrara el valor total del avance
#

#Importando.csv
df=pd.read_csv("train.csv")

print("OKEY! Archivo cargado correctamente")
#df guarda la variable
#Mostrando las primeras filas del dataframe."head devuelve un tope"
print(df.head())
#ME MUESTRA EL TOTAL POR FILAS Y COLUMNAS O LOS CUENTA "df.shape"
filas,columnas = df.shape
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

total_anios = df['YearBuilt'].count()
print(f"Cantidad de filas con año valido: {total_anios}")

# Analisis avanzado de datos
print("---Analisis Avanzado de Datos---")
filtro_avanzado=df['SaleCondition'] == 'Normal'
df_filtrado=df[filtro_avanzado]
#filtro_avanzado va buscando los filtros, ej "df_filtrado"
total_registros = df_filtrado['SaleCondition'].count()
print(f"Cantidad de veces que aparece NORMAL: {total_registros}")
#.2fsirve para ver  los centimos que vos queres que muestre
suma_dinero = df_filtrado['SalePrice'].sum()
print(f"Valor total de NOR es: {suma_dinero}")


# FILTRO EXACTO (esto sí cumple la consigna)
#filtro_avanzado = df['SaleCondition'] == 'Normal'
#df_filtrado = df[filtro_avanzado]

#total_registros = df_filtrado['SaleCondition'].count()
#print(f"Cantidad de veces que aparece NORMAL: {total_registros}")

#suma_dinero = df_filtrado['SalePrice'].sum()
#print(f"Valor total de NORMAL es: {suma_dinero:.2f}")