import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

ciudades = ['Valencia', 'Barcelona', 'Castellon']
codigo = ['123A', '456B', '789C']


myvar = pandas.DataFrame(mydataset)



if __name__ == '__main__':
  print(myvar)
  print(pandas.__version__)
