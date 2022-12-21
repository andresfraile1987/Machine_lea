
# Se importan la librerias que se necesitan en el programa
import pandas as pd
import numpy as np # Numpy no es necesario para este programa
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Se carga la información del archivo csv y se crea la variable objetivo
ventas = pd.read_csv("ventas2.csv")
objetivo = "monto"
# Se toman todas la columnas excepto monto
independientes = ventas.drop(columns=['monto']).columns
# Se crea el modelo de tipo regresión lineal
modelo = LinearRegression()
# Se ajusta el modelo indicando las columnas de entrenamineto y el dato objetivo
modelo.fit(X=ventas[independientes].values, y=ventas[objetivo]) # Se adicion la propiedad 'values' a los datos de entranamineto por un warning que se estaba generando

# Se adiciona la columna ventas predicciones desde el modelo con las columnas de entrenamiento 
ventas["ventas_prediccion"] = modelo.predict(ventas[independientes])
# Se definen los datos que se van a mostrar en la grafica tomados desde ventas 
preds = ventas[["monto", "ventas_prediccion"]].head(50)

# Se realiza la predicción de cuanto puede comprar un cliente y juargando en monto en una variable
talvez = modelo.predict([[41,1,1,1]])
# Se muestra en consola La cifra posible de compra
print ("Tal vez compre: ")
print (talvez)

# ***** Otra prueba de la predicción *****
# Se define un cliente con los dato 27 como edad, 2 en cantidad, 1 en vehículo y pago 1
cliente2 = [27,2,1,2]
# Se corre el algoritmo y se muestra la predicción
talvez = modelo.predict([cliente2])
print('***** Nuestro aplicacion de algoritmo *****')
print('El segundo cliente de 27 años, con un acompañante, es su vehículo y pagando en efectivo')
print(f'La predicción de compra para el segundo cliente es por un monto de ${talvez[0]}')

# Se genera la gráfica con los datos definidos en set de datos preds
# donde se compara el valor comprado y la predicción después del entrenamiento
preds.plot(kind='bar',figsize=(18,8))
plt.grid(linewidth='2')
plt.grid(linewidth='2')
plt.grid(None)
plt.show()
