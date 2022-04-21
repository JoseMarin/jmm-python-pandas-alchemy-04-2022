import pandas as pd

inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) + ': '))

print(ventas)

ventas = pd.Series(ventas)

if __name__ == '__main__':
    print('Ventas\n', ventas)
    print('Ventas con descuento\n', ventas * 0.9)
