import pandas as pd

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
filtro_avanzado=df['SaleCondition'].str.startswith('Nor', na=False)
df_filtrado=df[filtro_avanzado]
#filtro_avanzado va buscando los filtros, ej "df_filtrado"
total_registros = df_filtrado['SaleCondition'].count()
print(f"Cantidad de veces que aparece NORMAL: {total_registros}")
#.2fsirve para ver  los centimos que vos queres que muestre
suma_dinero = df_filtrado['SalePrice'].sum()
#print(f"Valor total de NOR es: {suma_dinero}")

print("--Reporte Automatizado--")
print(f"Valor total de NOR es: {suma_dinero:.2f}")

if Default_limite_alto:=(suma_dinero>500):
    print("Alerta: El volumen de mercado es Cirtico " \
    "y de alta prioridad.")
    print("Requiere revision inmediata")

elif suma_dinero > 200:
    print("Aviso: volumen mercado moderado/alto")
    print("Monitorzar comportamiento proximo trimestre")

else:
    print("Estado: volumen de mercado bajo a dentro del parametro")
    print("No se requiere accion adiccional")

