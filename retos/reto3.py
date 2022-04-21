import pandas as pd

# Funcion que recibe notas y realiza el calculo
def estadistica_notas(data):
    notas = pd.Series(data)
    print(notas)
    estadist = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    print(estadist)

# Metodo Main
if __name__ == '__main__':
    data = {'Juan': 9, 'Jose': 6.5, 'Diana': 4, 'Lola': 8.5, 'Fermin': 5}
    estadistica_notas(data)