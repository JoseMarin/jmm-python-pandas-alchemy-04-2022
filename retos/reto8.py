import pandas as pd

# pd.options.display.max_rows = 901
# pd.options.display.max_columns = 50
# pd.options.display.max_colwidth = 20

# Generar un DataFrame con los datos del fichero.
titanic = pd.read_csv('../data/titanic.csv', index_col=0)


if __name__ == '__main__':
    # print(titanic)

    # Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
    # los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
    # print('Dimensiones:', titanic.shape)
    # print('Número de elemntos:', titanic.size)
    # print('Nombres de columnas:', titanic.columns)
    # print('Nombres de filas:', titanic.index)
    # print('Tipos de datos:\n', titanic.dtypes)
    # print('Primeras 10 filas:\n', titanic.head(10))
    # print('Últimas 10 filas:\n', titanic.tail(6))

    # # Mostrar por pantalla los datos del pasajero con identificador 148
    # print(titanic.loc[300])
    #
    # # Mostrar por pantalla las filas pares del DataFrame.
    print(titanic.iloc[range(1,titanic.shape[0],2)])
    #
    # # Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
    # print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)
    # #
    # # # Alternativa
    # print(titanic['Survived'].value_counts(normalize=True) * 100)
    #
    # #Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
    # print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))
    #
    # # Eliminar del DataFrame los pasajeros con edad desconocida.
    # titanic.dropna(subset=['Age'])
    # print(titanic)
    # # Alternativa
    titanic = titanic[titanic['Age'].notna()]
    #
    # # Mostrar la edad media de las mujeres que viajaban en cada clase.
    # print(titanic.groupby(['Pclass', 'Sex'])['Age'].mean().unstack()['female'])
    #
    # # Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
    titanic['Young'] = titanic['Age'] < 18
    #
    # # Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
    print(titanic.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize=True) * 100)
    #
    titanic.to_csv('../storedata/titanic_procesed.csv', header=True, index=False)