import pandas as pd

pd.options.display.max_rows = 101
pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 20

df = pd.read_csv('../data/file3.csv')

if __name__ == '__main__':
  # print(df)
  # # print(df.loc["day2"]) # error
  # print(pd.__version__)

  print("---------------------------------------------------------------------------------------")
  rslt_df = df[df['gender']=='Female']
  # print(rslt_df)

  lista = rslt_df.values.tolist()

  # print(lista)

  df.values.tolist()
  #
  # lista2 = df['email'].tolist()
  # print(lista2)

  lista4 = df[['email', 'ip_address','gender']].query("gender=='Female'")
  lista4 = lista4.values.tolist()
  print(lista4)

  lista5 = df.query("gender=='Male' and ip_address=='252.82.166.20'")
  lista5 = lista5[['email', 'ip_address']].values.tolist()
  # print(lista5)

  newDf = pd.DataFrame(lista4, columns = ['email', 'ip_address','gender'])
  # print(newDf)
  newDf.to_csv('../data/file4.csv', header=True, index=False)





