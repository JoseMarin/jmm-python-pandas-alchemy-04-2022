import pandas as pd

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
         'Ventas':[30500, 35600, 28300, 33900],
         'Gastos':[22000, 23400, 18100, 20700]}

contabilidad = pd.DataFrame(datos)
# print(contabilidad)

def balance(newContabilidad, meses):
    newContabilidad['Balance'] = newContabilidad.Ventas - newContabilidad.Gastos
    print(contabilidad)
    newContabilidad.to_csv('../data/newContabilidad.csv', header=False, index=False)
    return newContabilidad[newContabilidad.Mes.isin(meses)].Balance.sum()



if __name__ == '__main__':

    print(balance(contabilidad,['Enero','Marzo']))

