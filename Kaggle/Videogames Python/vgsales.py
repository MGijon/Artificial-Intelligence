import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importamos los datos desde un archivo de excell
file = 'vgsales.csv'
datos = pd.read_csv(file)

# Visualizamos la cabecera para asegurarnos de  que la importación se ha realizado
# correctamente
datos.head()

# así podemos obtener los nombres de las colmnas del data.frame, en este caso se
# corresponden con los campos de lo sque tenemos datos
columnas = datos.columns
print(columnas)
# tenemos varias formas de extraer datos de un data frame:
datos.iloc[0][1]
datos.loc[0]['Name']
datos.at[0, 'Year']
datos.iat[0, 5]
datos.get_value(0, 'NA_Sales')
datos[columnas[3]]
datos['Rank']

# Estudiemos la relación (clara y directa por definición) entre las ventas globales,
# en Japón, Europa y EEUU y la posición del juego en el ranking
plt.scatter(datos['Rank'], datos['Global_Sales'], c = 'r', label = 'Global Sales', marker = '^' )
plt.scatter(datos['Rank'], datos['NA_Sales'], c = 'yellow', alpha = 0.5, label = 'American', marker = (5, 1))
plt.scatter(datos['Rank'], datos['EU_Sales'], c = 'green', alpha = 0.5, label = 'Europe', marker = ',')
plt.scatter(datos['Rank'], datos['JP_Sales'], c = 'blue', alpha = 0.5, label = 'Japan', marker = 'o')
plt.legend()
plt.title('Rank and sales in different markets')
plt.xlabel('Rank')
plt.ylabel('Sales')
plt.savefig('Rank-Sales.png')
plt.show()


# a la vista de los datos no me parece que una análisis lineal (regresión lineal)
# funcione del todo bien, pero voy a aplicarlo con las ventas en
