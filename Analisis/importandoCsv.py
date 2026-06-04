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

#------------------------------------------
#GRAFICO 1: Grafico de Barras (con Seaborn)
#------------------------------------------

#print("\n Generando Grafico de barras")

#sns.set_theme(style="whitegrid")

#plt.figure(figsize=(9,5))
#-LE ESTAS DEFINIENDO DIRECTAMENTE EL GRAFICO O LA ESTRUCTURA-
#-"viridis" sirve para alternar los colores, "magma", Blues_d
#sns.barplot(
#    data=df,
#    x="SaleCondition",
#    y="SalePrice",
#    estimator=sum,
#    errorbar=None,
#    palette="viridis",
#)
# Añadimos el titulo al grafico
#plt.title(
#    "Distribucion economica de tecnologia avanzada", fontsize = 14 
#)
#plt.xlabel("tipo de Condiccion", fontsize=11)
#plt.ylabel("Total (Precio Normal)", fontsize=11)

#plt.tight_layout()
#plt.savefig("grafico_barras.png", dpi=300)
#plt.xticks(rotation=40, fontsize=8)
#plt.show()
#plt.close()
#("Grafico de barras guardado exitosamente. ")
#------------------------------------
#GRAFICO DE TORTAS
#------------------------------------

print("\n Generando Graficos de Torta ")

datos_torta =(
     df.groupby("SaleCondition")["SalePrice"]
     .sum()
     .nlargest(5)
) 

plt.figure(figsize=(7,7))
plt.pie(
     datos_torta.values,
     labels=datos_torta.index,
     autopct="%1.1f%%",
     colors=sns.color_palette("Set2")[0:5],
     startangle=148,
     wedgeprops={'edgecolor':'white','linewidth':2},
     # Agrega solo estas 3 líneas aquí abajo:
     pctdistance=0.75,          # Acerca los porcentajes al centro de cada porción
     labeldistance=1.15,        # Empuja los nombres hacia afuera del círculo para que no se pisen
     textprops={'fontsize': 9}  # Achica un poco la letra para dar más espacio
)

plt.title("Distribucion interna: Tegnologia Avanzada", fontsize=14)
plt.savefig("grafico_torta.png", dpi=300)
plt.close()
print("Grafico de torta guardado exitosamente. ")