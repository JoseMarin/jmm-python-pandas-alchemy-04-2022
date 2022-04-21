import pandas as pd

df = pd.read_csv('../data/file3b.csv', sep='|')
df2 = pd.read_csv('../data/file3.csv')

suma = pd.concat([df, df2])



if __name__ == '__main__':
  print(suma)

  