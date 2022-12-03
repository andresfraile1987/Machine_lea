"""
Actividad 3
ETL en Python

Estudiantes: 
Alberson Johan Sánchez Garavito
Andrés Ricardo Fraile Blanco

Corporación Unificada Nacional De Educación Superior (CUN)
Ficha: 60101, 
Diplamado Machine learning en Python
Docente: Ing. Luis Enrique Camargo Camargo
Diciembre 02 del 2022

"""

# Importacion de la librerias de Pandas y Requests
import pandas as pd
import requests as rq

# Llave para acceder al API
api_key = 'c5b1862985a2a3f19e175e42b0380450'


# ****** EXTRACCIÓN ******

# Se crean unas listas se de usaran durante la extracción 
response_list = []
result = []

# Aunque la base de datos tiene muchos registros solo se van a usar 9 para este ejemplo
# Se genera un ciclo para llamar cada uno de los registros a través de API
# y se agrega a la lista para tener todods los registros en la lista 
for movie_id in range(550,556): 
  url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, api_key)
  r = rq.get(url)
  response_list.append(r.json())
  
# Se convierte la lista de los registros obtenidos 
# de API a un DataFranme de Pandas
df = pd.DataFrame.from_dict(response_list)

# ****** TRANSFORMACIÓN ******

# Se definen las columnas que se van a utilizar
df_columns = ['budget', 'genres', 'id', 'imdb_id', 'original_title', 'release_date', 'revenue', 'runtime']

# Se eliminan los titulos que son duplicados de DataFrame
df = df.drop_duplicates('original_title')

# Se toman los datos de la columna genres y se conviente en una lista y 
# se convierten los diccionarios en una lista de dos columnas 
genres_list = df['genres'].tolist()
flat_list = [item for sublist in genres_list for item in sublist]

# Se recorre el listado de generos y agrupan solo los nombres 
# para adicionarlos la Datafreme principal como la columna genres_all
for l in genres_list:
    r = []
    for d in l:
        r.append(d['name'])
    result.append(r)
df = df.assign(genres_all=result)

# Se crea otra DataFrame a partir de listado de dos columnas
# y se eliminan los duplicados
df_genres = pd.DataFrame.from_records(flat_list).drop_duplicates()

# Se redefinen las columnas que se van a usar para el cargue, ya que genres no se necesitara
# también, se crea una lista con los nombres de los generos y se adiciona al listado de columna redefinido 
df_columns = ['budget', 'id', 'imdb_id', 'original_title', 'release_date', 'revenue', 'runtime']
df_genre_columns = df_genres['name'].to_list()
df_columns.extend(df_genre_columns)

# Se define por cada registro que generos le corresponden 
# y se le adiciona al DataFrame principal como columnas 
# colonacdo 1 si corresponde o 0 si no
s = df['genres_all'].explode()
df = df.join(pd.crosstab(s.index, s))

# Se convierte la columna release_date en fecha y hora
# y con base en ella se crea el dato de día, mes, año y día de la semana
# adicional, se crea la lista de los columna para la tabla 
df['release_date'] = pd.to_datetime(df['release_date'])
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year
df['day_of_week'] = df['release_date'].dt.day_name()
df_time_columns = ['id', 'release_date', 'day', 'month', 'year', 'day_of_week']

# ****** CARGUE ******

# Se filtra el Dataframe principal con las columnas a cargar 
# y se convierte en un archivo CSV y se guarda en la misma carpeta
# se realiza lo mismo para convertir en CSV el Data frame principal 
# filtrado por las columnas de calendario
# y se convierte en CSV el Dataframe de generos
df[df_columns].to_csv('tmdb_movies.csv', index=False)
df_genres.to_csv('tmdb_genres.csv', index=False)
df[df_time_columns].to_csv('tmdb_datetimes.csv', index=False)