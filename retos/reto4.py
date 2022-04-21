import pandas as pd

# Funcion que recibe notas y realiza el calculo
def estadistica_notas(data):
    notas = pd.Series(data)
    # print(notas)
    aprob = notas[notas >= 5].sort_values(ascending=False)
    # # aprob = notas['Juan']
    print(aprob)

# Metodo Main
if __name__ == '__main__':
    data = {'Juan': 9, 'Jose': 6.5, 'Diana': 4, 'Lola': 8.5, 'Fermin': 5}
    estadistica_notas(data)