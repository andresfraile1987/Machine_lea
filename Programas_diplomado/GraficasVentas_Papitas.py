
# Se importan las librerías que se usaran en el programa
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Se obtienen los datos de archivo PRODUCTO de Excel sin las 2 primeras filas
# y se cargan en un DataFrame temporal
temp_productos_df = pd.read_excel('PRODUCTOS.xlsx',sheet_name='Hoja1', skiprows=[0,1])
# Se crea un DataFrame vacío con un Id y Producto como columnas
productos_df = pd.DataFrame(columns=['ProductoId','Producto'])
# Se crea un DataFrame vacío con un Id, Referencia, Medida, ValorUnd, Id del producto como columnas
referencias_df = pd.DataFrame(columns=['ReferenciaId','Referencia','Medida','ValorUnd','ProductoId'])
# Se recorren los registros del DataFrame temporal para llenar los DataFrames de productos y referencias
for i in range(len(temp_productos_df)):
    productos_df.loc[len(productos_df.index)] = [len(productos_df.index)+1,temp_productos_df.iloc[i,0]]
    referencias_df.loc[len(referencias_df.index)] = [((len(referencias_df.index)+1)*10)+len(productos_df.index),temp_productos_df.iloc[i,0]+'-'+temp_productos_df.iloc[i,1],temp_productos_df.iloc[i,2],temp_productos_df.iloc[i,3],len(productos_df.index)]
    referencias_df.loc[len(referencias_df.index)] = [((len(referencias_df.index)+1)*10)+len(productos_df.index),temp_productos_df.iloc[i,0]+'-'+temp_productos_df.iloc[i,4],temp_productos_df.iloc[i,5],temp_productos_df.iloc[i,6],len(productos_df.index)]
    referencias_df.loc[len(referencias_df.index)] = [((len(referencias_df.index)+1)*10)+len(productos_df.index),temp_productos_df.iloc[i,0]+'-'+temp_productos_df.iloc[i,7],temp_productos_df.iloc[i,8],temp_productos_df.iloc[i,9],len(productos_df.index)]

# Se obtienen los datos de ventas de los dos meses en un DataFrame de ventas
ventas_df = pd.read_excel('VentasMeses1y2.xlsx',sheet_name='VentasMeses1y2')
# Función para obtener el nombre de la referencia a través del id de referencia en el DataFrame de referencias
referencias = lambda row: referencias_df.loc[referencias_df['ReferenciaId']==row['Referencia'],'Referencia'].iloc[0]
# Función para obtener el valor unitario a través del id de referencia en el DataFrame de referencias
valorund = lambda row: referencias_df.loc[referencias_df['ReferenciaId']==row['Referencia'],'ValorUnd'].iloc[0]
# Función para obtener el id del producto a través del id de referencia en el DataFrame de referencias
productoid = lambda row: referencias_df.loc[referencias_df['ReferenciaId']==row['Referencia'],'ProductoId'].iloc[0]
# Función para obtener el nombre del producto a través del id de producto en el DataFrame de productos
producto = lambda row: productos_df.loc[productos_df['ProductoId']==row['ProductoId'], 'Producto'].iloc[0]
# Se crea una nueva columna con los nombres de las referencias en el DataFrame de ventas usando una función
ventas_df['NombreRef'] = ventas_df.apply(lambda row: referencias(row), axis=1)
# Se crea una nueva columna con los valores unitarios de las referencias en el DataFrame de ventas usando una función
ventas_df['ValorUnd'] = ventas_df.apply(lambda row: valorund(row), axis=1)
# Se crea una nueva columna con los id de producto de las referencias en el DataFrame de usando una función
ventas_df['ProductoId'] = ventas_df.apply(lambda row: productoid(row), axis=1)
# Se crea una nueva columna con los nombres del producto en el DataFrame de ventas usando una función
ventas_df['Producto'] = ventas_df.apply(lambda row: producto(row), axis=1)
# Se crea una nueva columna con multiplicando la cantidad con el valor unitario en el DataFrame de ventas
ventas_df['TotalVentas'] = ventas_df['Cantidad']*ventas_df['ValorUnd']

# ***** Ventas por Producto *****
# Manejo del modelo para obtener datos para el gráfico
# Se obtiene la suma de la columna total ventas
grantotal = round(ventas_df['TotalVentas'].sum(),2)
# Se crea el DataFrame ventas producto a partir de agrupar y sumar el DataFrame de ventas
ventas_producto = ventas_df[['TotalVentas','Producto']].groupby('Producto').sum().reset_index()
# Función para obtener el porcentaje de total ventas sobre la variable gran total
porcentaje = lambda row: round(row['TotalVentas']/grantotal*100,2)
# Se crea una nueva columna con los porcentajes en el DataFrame ventas producto usando una función
ventas_producto['Porcentaje'] = ventas_producto.apply(lambda row: porcentaje(row),axis=1)
# Se ordena el DataFrame descendentemente por la columna porcentaje
ventas_producto = ventas_producto.sort_values('Porcentaje', ascending=False)

# Construir la figura con dimensiones especificas
fig = plt.figure(figsize=(10,12))
# Construir la maya principal con 1 fila y 1 columna
gs_master = mpl.gridspec.GridSpec(1,1,hspace=0, wspace=0, left=0.17)

# Se construye un maya de subplot para colocar las gráficas en 3 filas y 2 columnas
gs_1 = mpl.gridspec.GridSpecFromSubplotSpec(3, 2,hspace=0.25, subplot_spec=gs_master[0, :])
# Se construye un submaya de subplot para colocar el título, subtítulo y el periodo de tiempo
gs_11 = mpl.gridspec.GridSpecFromSubplotSpec(6, 1, subplot_spec=gs_1[0, 0])
# Se crea los contenedores de los gráficos y se le indican la ubicación dentro de la maya
venprod_axes = fig.add_subplot(gs_1[0, 1])
mesvsmes_axes = fig.add_subplot(gs_1[1, :])
venref_axes = fig.add_subplot(gs_1[2, :])

# Se crea los contenedores de los gráficos y se le indican la ubicación dentro de la submaya
title_axes = fig.add_subplot(gs_11[2])
subtitle_axes = fig.add_subplot(gs_11[3])
months_axes = fig.add_subplot(gs_11[4])

# Se crea el título y se remueven los vértices y etiquetas
title_axes.set_title("Papitas SAS", fontsize = 30, color = "#5f86fa")
title_axes.set_frame_on(False)
[n.set_visible(False) for n in title_axes.get_xticklabels() + title_axes.get_yticklabels()]
[n.set_visible(False) for n in title_axes.get_xticklines() + title_axes.get_yticklines()]

# Se crea el subtítulo y se remueven los vértices y etiquetas
subtitle_axes.set_title("Junta Directiva - Ventas", fontsize = 20, color = "#9ab3fc")
subtitle_axes.set_frame_on(False)
[n.set_visible(False) for n in subtitle_axes.get_xticklabels() + subtitle_axes.get_yticklabels()]
[n.set_visible(False) for n in subtitle_axes.get_xticklines() + subtitle_axes.get_yticklines()]

# Se crea el periodo y se remueven los vértices y etiquetas
months_axes.set_title("Mes 1 y Mes 2", fontsize = 16, color = "#9ab3fc")
months_axes.set_frame_on(False)
[n.set_visible(False) for n in months_axes.get_xticklabels() + months_axes.get_yticklabels()]
[n.set_visible(False) for n in months_axes.get_xticklines() + months_axes.get_yticklines()]

# Crear el gráfico de torta para Ventas por producto
venprod_axes.pie(ventas_producto['Porcentaje'],labels=ventas_producto['Producto'], 
        autopct='%1.1f%%', pctdistance=0.85)
# Dibujar un círculo blanco
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# Agregar el círculo al gráfico
venprod_axes.add_artist(centre_circle)
# Agregar el título
venprod_axes.set_title('Ventas por Producto')

# ***** Ventas por Referencia *****
# Manejo del modelo para obtener datos para el gráfico
# Se crea el DataFrame ventas referencia a partir de agrupar y sumar el DataFrame de ventas
ventas_referencia = ventas_df.groupby(['Referencia','NombreRef'], as_index=False)['TotalVentas'].sum()
# Se ordena el DataFrame ascendentemente por la columna porcentaje
ventas_referencia = ventas_referencia.sort_values('TotalVentas', ascending=True)

# Obtener colores diferentes para cada barra del gráfico
colors = plt.cm.Dark2(range(6))

# Crear las barras para el gráfico con las etiquetas, valores y colores
venref_axes.bar(ventas_referencia['NombreRef'],ventas_referencia['TotalVentas'], color=colors)
# Se define el título la etiqueta del eje 'y' para el gráfico
venref_axes.set_title('Ventas por Referencia (Valores en millones)')
venref_axes.set_ylabel('Ventas')

# Función para agregar el valor a cada barra
def add_value_labels(ax, spacing=1):
    # Recorre cada barra
    for rect in ax.patches:
        # Se define donde se coloca el valor
        y_value = rect.get_height()*0.8
        x_value = rect.get_x() + rect.get_width() / 2
        # Se define el especio entre la barra y el valor
        space = spacing
        # Alineación vertical para número positivos
        va = 'bottom'
        # Cuando el valor es negativo se coloca el valor hacia abajo
        if y_value < 0:
            # Se invierte es espacio para colocar el valor abajo
            space *= -1
            # Alineación vertical hacia arriba
            va = 'top'
        # Da formato al valor
        label = round(y_value/1000000,3)
        # Crea la anotación
        ax.annotate(
            label,                      # EL valor para la barra
            (x_value, y_value),         # Ubicación del valor
            xytext=(0, space),          # Desplazamiento vertical del valor
            textcoords='offset points', # Interprete de xytext
            ha='center',                # Valor centrado horizontal 
            va=va)
# Llamado de la función con el eje
add_value_labels(venref_axes)
# Etiquetas del eje x se rotan y se alinean hacia la izquierda
venref_axes.set_xticklabels(venref_axes.get_xticklabels(),rotation=30, ha='right',rotation_mode='anchor')

# ***** Ventas por Referencia mes 1 contra mes 2 *****
# Manejo del modelo para obtener datos para el gráfico
# Se crea el DataFrame ventas referencia mes 1 a partir de filtrar los datos del mes 1, agrupar por referencia y sumar el DataFrame de ventas
ventas_referencia_mes1 = ventas_df.query("Mes == 1").groupby(['Referencia','NombreRef'], as_index=False)['TotalVentas'].sum()
# Se cambia el nombre de la columna por mes 1
ventas_referencia_mes1.rename(columns = {'TotalVentas':'Mes1'}, inplace=True)
# Se crea el DataFrame ventas referencia mes 2 a partir de filtrar los datos del mes 1, agrupar por referencia y sumar el DataFrame de ventas
ventas_referencia_mes2 = ventas_df.query("Mes == 2").groupby(['Referencia','NombreRef'], as_index=False)['TotalVentas'].sum()
# Se cambia el nombre de la columna por mes 2
ventas_referencia_mes2.rename(columns = {'TotalVentas':'Mes2'}, inplace=True)
# Se unen los dos DataFrame con dos columnas coincidentes
ventas_referencia_mes = pd.merge(ventas_referencia_mes1, ventas_referencia_mes2, on=['Referencia','NombreRef'])
# Se ordenan los datos por la columna mes 1 descendentemente
ventas_referencia_mes = ventas_referencia_mes.sort_values('Mes1', ascending=True)

# --- Se crea el grafico que se adiciona al dashboard ---
# Se crea una lista de los índices del DataFrame y se define el ancho las barras
ref = np.arange(len(ventas_referencia_mes['NombreRef']))
wid_bar = 0.2

# Se crean las barras del mes 1 y el mes 2 
rects1 = mesvsmes_axes.barh(ref+wid_bar/2,ventas_referencia_mes['Mes1'], wid_bar,label='Mes 1')
rects2 = mesvsmes_axes.barh(ref-wid_bar/2,ventas_referencia_mes['Mes2'], wid_bar,label='Mes 2')

# Se define el título del gráfico y la etiqueta del eje 'x'
mesvsmes_axes.set_title('Ventas por Referencia Mes 1 vs Mes 2 (Valores en millones)')
# se colocan los nombres de las referencias
mesvsmes_axes.set_yticks(ref, ventas_referencia_mes['NombreRef'])
# Se adiciona las leyendas para saber cu's'les son los datos de cada mes
mesvsmes_axes.legend()
# Se ajusta la figura al layout
fig.tight_layout()

# Se ordenan los datos por la columna mes 1 descendentemente
ventas_referencia_mes = ventas_referencia_mes.sort_values('Mes1', ascending=False)
# se define el nombre de referencia como el índice del DataFrame
ventas_referencia_mes.set_index('NombreRef', inplace=True)

# --- Se crea una alternativa del grafico que no se adiciona al dashboard ---
# Crear un subplot con 2 columna con eje y coincidente
fig, axes = plt.subplots(figsize=(10,5), ncols=2, sharey=True)
# Adicionar el título del gráfico
fig.suptitle('Ventas por Referencia Mes 1 vs Mes 2 (Valores en millones)')

# se preparan datos para el gráfico
index = ventas_referencia_mes.index
column0 = ventas_referencia_mes['Mes1']
column1 = ventas_referencia_mes['Mes2']

# Crear el subgráfico una para la primera columna y se te asigna un título
axes[0].barh(index, column0, align='center', color='r', zorder=10)
axes[0].set_title('Mes 1', pad=5, color='r')
# Crear el subgráfico una para la segunda columna y se te asigna un título
axes[1].barh(index, column1, align='center', color='g', zorder=10)
axes[1].set_title('Mes 2', pad=5, color='g')

# Invertir en el eje (x) del grafico de la primera columna
axes[0].invert_xaxis()
# Invertir el eje (y) para el mismo gráficos
plt.gca().invert_yaxis()

# Se colocan los nombres de las referencias
axes[0].set(yticks=ventas_referencia_mes.index, yticklabels=ventas_referencia_mes.index)
# Mueve as etiquetas del eje 'y' hacia la izquierda
axes[0].yaxis.tick_left()

# Se ajusta el subplot para que se vea correctamente
plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)

# Se muestran el dashboard y el gráfico alternativo
plt.show()


''' 
Conclusiones

De la gráfica de dona se concluye que, aunque las ventas presentan un comportamiento relativamente 
similar, las papas fritas se quedan rezagadas y por lo tanto se debería iniciar una campaña 
publicitaría tanto en redes como en medios de comunicación masivos como TV y radio para incentivar 
su consumo sin descuidar obviamente los demás productos.

En la gráfica de barras horizontales, se observa estabilidad en la mayoría de productos, resaltando 
el crecimiento del consumo de los plátanos en su referencia dulce, dado este crecimiento se estima 
que seguirá la misma curva y por lo tanto se destinaran más recursos económicos y de mano de obra 
para su producción para anticiparnos a la demanda del mes de diciembre.

Por último, en gráfica de barras verticales podemos ver que el chicharrón blanco supera ampliamente 
las ventas de los demás productos y, en sus otras presentaciones ocupa los primeros lugares, se 
pronostica un crecimiento notable en las ventas de este producto por la temporada del mundial así 
que se verificará y se ajustará el inventario de los insumos correspondientes para cumplir con la demanda.

'''