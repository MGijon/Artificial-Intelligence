import gensim.models as gm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sn

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

words = list(model.vocab.keys())[:1000]

data = pd.DataFrame()
data['words'] = words
data['values'] = [model.most_similar( positive = ['women', i],
                  negative = ['men'], topn = 1)[0][1] for i in data['words']]

data.to_csv('Data/Concept_proof.csv', index = False)

####################################

datos = pd.read_csv('Data/Concept_proof.csv')
valores = datos['values']
len(valores)

## Histograma:
## ==========

# hacemos una primera visualización de los datos mediante un simple histograma
plt.figure(figsize = (10, 7.5))
plt.xlabel('Distancias por la relación de género')
plt.ylabel('Número de muestras')
plt.title('Gender bias 1000 first words')
valores.plot(kind = 'hist', bins = 50)
plt.savefig('Data/1000_words_histogram.png')
plt.show()


## Distribution plot:
## =================

# visualizamos la distribición que siguen los datos:
plt.figure(figsize = (10, 7.5))
plt.xlabel('Distancias por la relación de género')
plt.ylabel('Número de muestras')
plt.title('Gender bias 1000 first words')
sn.distplot(valores)
plt.savefig('Data/1000_words_distplot.png')
plt.show()


## Distribución de frecuencias:
## ===========================

# cremos los intervalos:
intervalos = np.arange(0., 1., .1)
# introducimos los datos en cada intervalo:
frecuencias = pd.cut(valores, intervalos)
# construimos la tabla de frecuencia contando los valores por intervalo:
tabla_de_frecuencia = pd.value_counts(frecuencias)
print(tabla_de_frecuencia)

## Medias de tendencia central:
## ===========================

# (1) Media aritmética:
# ---

print(valores.mean())

# (2) Media geométrica:
# ---

print(stats.gmean(valores))

# (3) Media armónica:
# ---

print(stats.hmean(valores))

# (4) Mediana:
# ---

print(valores.median())

# (5) Moda:
# ---

print(valores.mode())

# (6) Media truncada:
# ---

print(stats.trim_mean(valores, .1))

# (7) Kurtosis:
# ---

print(stats.kurtosis(valores))

# (8) Simetría:
# ---

print(stats.skew(valores))


## Medias de dispersión:
## ====================

# (1) Varianza:
# ---

print(valores.var())

# (2) Desviación estándard:
# ---

print(valores.std())

# (3) Cuartiles:
# ---

print(valores.quantile([.25, .5, .75]))

# (4) Box plot:
# ---

plt.figure(figsize = (10, 7.5))
plt.title('Gender bias 1000 first words')
sn.boxplot(valores)
plt.savefig('Data/1000_words_boxplot.png')
plt.show()

## Resumen estadístico:
## ===================

print(valores.describe())

## Otros:
## =====

# (1) Violin plot:
# ---

plt.figure(figsize = (10, 7.5))
plt.title('Gender bias 1000 first words')
pal = sn.cubehelix_palette(8, rot = -.5, dark = .3)
sn.violinplot(data = valores, palette = pal, inner = "points")
plt.savefig('Data/1000_words_violinplot.png')
plt.show()

# (2) Distplot with rug = True
# ---

plt.figure(figsize = (10, 7.5))
plt.title('Gender bias 1000 first words')
sn.distplot(valores, rug = True)
plt.savefig('Data/1000_words_Rug_distplot.png')
plt.show()

# (3) Kernel density estimation
# ---

plt.figure(figsize = (10, 7.5))
plt.title('Gender bias 1000 first words')
sn.distplot(valores, hist = False, rug = True)
plt.savefig('Data/1000_words_Kernel.png')
plt.show()
