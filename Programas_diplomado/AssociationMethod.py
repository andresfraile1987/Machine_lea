# Se debe instalar el paquete mlxtend para poder correr este código
# Este el el comando que se debe ejecutar desde la consola:
# pip install mlxtend

# Se importan las librerías necesaria para el programa
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Se crea un dataframe con los datos leidos del archivo en Excel 
# que se utilizara para alimentar el algoritmo
df = pd.read_excel("Online_Retail.xlsx")

# Se empieza a limpiar los datos comenzando por remuever los 
# espacios en blanco en el principio y en el final de las descripciones
df['Description'] = df['Description'].str.strip()

# Se remueven los registros donde el número de Invoice sea nulo
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

# Se convierte los datos de la columna de número de invoice a string
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
# Remover las factura que contengan C que son las que tiuene credito
df = df[~df['InvoiceNo'].str.contains('C')]

# Ventas realizadas en Francia, agrupa por invoice y convierte los productos en columnas creando una matriz
basket_FR = (df[df['Country']=='France'].groupby(['InvoiceNo','Description'])['Quantity'].
          sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
# Ventas realizadas en Portugal y convierte los productos en columnas creando una matriz
basket_PT = (df[df['Country']=='Portugal'].groupby(['InvoiceNo','Description'])['Quantity'].
          sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
# Ventas realizadas en Suecia y convierte los productos en columnas creando una matriz
# basket_SE = (df[df['Country']=='Sweden'].groupby(['InvoiceNo','Description'])['Quantity'].
#           sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))

# Función para convierte las cantidades en 0 y 1 para llenar la matriz
def hot_encode(x):
    if(x<=0):
        return 0
    if(x>=1):
        return 1

# Se crea la matriz codificada de productos colocando 1 cuando la 
# venta tuvo el producto y se llena la matriz de las ventas del pais 
# de acuerdo la matriz codificada
basket_encoded = basket_FR.applymap(hot_encode)
basket_FR = basket_encoded
# Se realiza lo mismo para la matriz de Portugal
basket_encoded = basket_PT.applymap(hot_encode)
basket_PT = basket_encoded
# Se realiza lo mismo para la matriz de Suecia
# basket_encoded = basket_SE.applymap(hot_encode)
# basket_SE = basket_encoded

# Se crea el modelo de frecuencia por producto con los datos de de ventas 
# por país donde el soporte sea mayor a 5%
frq_items_FR = apriori(basket_FR, min_support = 0.05, use_colnames = True)
frq_items_PT = apriori(basket_PT, min_support = 0.05, use_colnames = True)
# frq_items_SE = apriori(basket_SE, min_support = 0.05, use_colnames = True)
  
# Se definen las reglas de asociación con base en el modelo y donde el 
# peso 'lift' sea mayor a 1 por país
rules_FR = association_rules(frq_items_FR, metric ="lift", min_threshold = 1)
rules_PT = association_rules(frq_items_PT, metric ="lift", min_threshold = 1)
# rules_SE = association_rules(frq_items_SE, metric ="lift", min_threshold = 1)

# Se ordenan descendentemente por la confidencia y el peso, es decir 
# que se ordena de los productos con mayor valores las dos columnas 
# por cada país
rules_FR = rules_FR.sort_values(['confidence', 'lift'], ascending =[False, False])
rules_PT = rules_PT.sort_values(['confidence', 'lift'], ascending =[False, False])
# rules_SE = rules_SE.sort_values(['confidence', 'lift'], ascending =[False, False])

# Se muestra los resultados para las tiendas en Francia
print('\n************************************')
print('Estas son las cinco primeras reglas')
print('de asociación para Francia')
print(rules_FR.head())
# Se muestra los resultados para las tiendas en Portugal
print('\n************************************')
print('Estas son las cinco primeras reglas')
print('de asociación para Portugal')
print(rules_PT.head())
# Se muestra los resultados para las tiendas en Suecia
# print(rules_SE.head())