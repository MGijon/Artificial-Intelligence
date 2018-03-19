import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Import the data:
## ===============

path_pokemon = 'Data/pokemon.csv'
path_combats = 'Data/combats.csv'
path_tests = 'Data/tests.csv'

pokemon = pd.read_csv(path_pokemon)
print(pokemon.head())

combats = pd.read_csv(path_combats)
print(combats.head())

tests = pd.read_csv(path_tests)
print(tests.head())
