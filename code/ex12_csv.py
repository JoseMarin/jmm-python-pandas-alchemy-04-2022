import pandas as pd

pd.options.display.max_rows = 101
pd.options.display.max_columns = 50
# pd.options.display.max_colwidth = 20

df = pd.read_csv('../data/file3.csv')

if __name__ == '__main__':
  print(df)

  