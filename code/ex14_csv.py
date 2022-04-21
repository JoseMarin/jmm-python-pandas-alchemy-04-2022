import pandas as pd

pd.options.display.max_rows = 101
pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 20

df = pd.read_csv('../data/file3.csv')

if __name__ == '__main__':
  print(df)
  # print(df.loc["day2"]) # error
  print(pd.__version__)

  print("---------------------------------------------------------------------------------------")
  rslt_df = df[df['gender']=='Male']
  print(rslt_df)
  