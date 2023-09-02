# Crea una Serie de los numeros 10, 20 and 10.
import pandas as pd

serie = pd.Series([10, 20, 10])
print(serie)

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
import pandas as pd

objetos = pd.Series(['rojo', 'verde', 'azul'])
print(objetos)

## Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
import pandas as pd

df = pd.DataFrame({'columna1': [1, 2, 3]})  
serie_numeros = pd.Series([10, 20, 10])
df['columna2'] = serie_numeros
print(df)

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
import pandas as pd
df = pd.DataFrame({'columna1': [1, 2, 3]})  
colores = pd.Series(['rojo', 'verde', 'azul'])
df['columna2'] = colores
print(df)

## Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
import pandas as pd
ruta_archivo = r'C:\Users\Nicole\Documents\src\avengers.csv'
avengers = pd.read_csv(ruta_archivo)
print(avengers)

# Muestra las primeras 5 filas del DataFrame 'avengers'
filas = avengers.head(5)
print(filas)

# Muestra las primeras 10 filas del DataFrame 'avengers'
filas10 = avengers.head(10)
print(filas10)

# Muestra las últimas 5 filas del DataFrame 'avengers'
filas5 = avengers.tail(5)
print(filas5)

# Muestra el tamaño del DataFrame 'avengers'
tamañodf = avengers.shape
print(tamañodf)

# Muestra los data types del dataframe
data = avengers.dtypes
print(data)


