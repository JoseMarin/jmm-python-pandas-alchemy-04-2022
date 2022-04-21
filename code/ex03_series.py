import pandas as pd

# a = [1, 7, 2]

ciudades = ['Valencia', 'Barcelona', 'Castellon']
codigo = ['123A', '456B', '789C']

myvar = pd.Series(ciudades, index = codigo)



if __name__ == '__main__':
  print(myvar)
  # print(myvar["y"])
  # print(pd.__version__)
  