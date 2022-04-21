import pandas as pd

datos = {
         'Ventas':[30500, 35600, 28300, 33900],
         'Gastos':[22000, 23400, 18100, 20700]}

contabilidad = pd.DataFrame(datos,  index = ['Enero', 'Febrero', 'Marzo', 'Abril'])

if __name__ == '__main__':
    print(contabilidad)