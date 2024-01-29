"""
# ETL - Saber 11 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Saber_11__2019-2.csv')
newdata = data
columnas = ["ESTU_MCPIO_RESIDE", "COLE_NATURALEZA","FAMI_TRABAJOLABORMADRE","FAMI_SITUACIONECONOMICA","COLE_CALENDARIO","FAMI_TRABAJOLABORPADRE", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "ESTU_GENERO", "ESTU_TIENEETNIA", "ESTU_NACIONALIDAD","PUNT_GLOBAL","COLE_NOMBRE_ESTABLECIMIENTO"]
for column in data.columns:
  if column not in columnas:
    data = data.drop(column, axis=1)
data.head()
#newdata.head()

#newdata.info()
data.info()

categorical_columns = ["ESTU_MCPIO_RESIDE", "COLE_NATURALEZA","FAMI_TRABAJOLABORMADRE","FAMI_SITUACIONECONOMICA","COLE_CALENDARIO","FAMI_TRABAJOLABORPADRE", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "ESTU_GENERO", "ESTU_TIENEETNIA", "ESTU_NACIONALIDAD"]
for column in categorical_columns:
  data[column].value_counts().plot(kind = "bar")
  plt.show()

"""data["PUNT_GLOBAL"].plot(kind="box")"""

for column in data.columns[0:11]:
  data[column].replace({"-":None,"No sabe":None ,"No aplica":None,"Sin Estrato":None,"EXTRANJERO":None}, inplace=True)

data[data['PUNT_GLOBAL'] > 500] == None
data.info()

for column in data.columns[0:11]:
  data[column] = data[column].astype("category")

from sklearn.impute import SimpleImputer
categoricalImputer = SimpleImputer(missing_values=np.nan,strategy="most_frequent")
numericalImputer = SimpleImputer(missing_values= np.nan,strategy='mean')

categorical_columns = ["ESTU_MCPIO_RESIDE", "COLE_NATURALEZA","FAMI_TRABAJOLABORMADRE","FAMI_SITUACIONECONOMICA","COLE_CALENDARIO","FAMI_TRABAJOLABORPADRE", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "ESTU_GENERO", "ESTU_TIENEETNIA", "ESTU_NACIONALIDAD"]
for column in categorical_columns:
    data[column] = categoricalImputer.fit_transform(data[[column]])

data['PUNT_GLOBAL'] = numericalImputer.fit_transform(data[['PUNT_GLOBAL']])
data.info()

categorical_columns = ["ESTU_MCPIO_RESIDE", "COLE_NATURALEZA","FAMI_TRABAJOLABORMADRE","FAMI_SITUACIONECONOMICA","COLE_CALENDARIO","FAMI_TRABAJOLABORPADRE", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "ESTU_GENERO", "ESTU_TIENEETNIA", "ESTU_NACIONALIDAD"]
for column in categorical_columns:
  data[column].value_counts().plot(kind = "bar")
  plt.title(column)
  plt.show()

#print(len(data))

# Identificar y contar duplicados
duplicates = data[data.duplicated()]
duplicate_count = len(duplicates)

# Eliminar duplicados (si es necesario)
data = data.drop_duplicates()

print(f'Número de duplicados encontrados: {duplicate_count}')
print(f'Tamaño del conjunto de datos sin duplicados: {len(data)}')

data.info()

import random
registros_a_eliminar = 433143
total_registros = len(data)
#print(total_registros)
# Genera una lista de índices aleatorios de registros a eliminar.
indices_a_eliminar = random.sample(range(total_registros), registros_a_eliminar)

indices_a_eliminar = [i for i in indices_a_eliminar if i in data.index]

# Elimina los registros seleccionados aleatoriamente del DataFrame.
data = data.drop(indices_a_eliminar)
data.info()

categorical_columns = ["ESTU_MCPIO_RESIDE", "COLE_NATURALEZA","FAMI_TRABAJOLABORMADRE","FAMI_SITUACIONECONOMICA","COLE_CALENDARIO","FAMI_TRABAJOLABORPADRE", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "ESTU_GENERO", "ESTU_TIENEETNIA", "ESTU_NACIONALIDAD"]
for column in categorical_columns:
  data[column].value_counts().plot(kind = "bar")
  plt.show()

data["PUNT_GLOBAL"].plot(kind="box")

data.to_csv('./saber_11.csv')
