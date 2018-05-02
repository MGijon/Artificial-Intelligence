import pandas as pd

data = pd.read_csv('Data/concejales_historico.csv', sep = ';')

data.describe()

#data['Duración'] = data['Fecha de cese'] - data['Fecha de posesión']

# mirar como manejar fechas en python !!!!

for i in set(data['Grupo municipal/Lista electoral']):
    print(i)

data['Nombre completo'] = data['Nombre'] + ' ' + data['Apellidos']

data.describe()

len(data['Nombre completo']) / len(set(data['Nombre completo']))
