import pandas as pd 

df = pd.read_csv('Data/Concept_proof5')

print(type(df['Word_vector'][0]))

print(df['Word_vector'][0])
