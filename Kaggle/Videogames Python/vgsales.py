import pandas as pd

file = 'vgsales.csv'

datos = pd.read_csv(file)

datos.head()

columnas = datos.columns
print(columnas)
datos[columnas[2]
