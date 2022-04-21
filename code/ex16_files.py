import os
import shutil

import pandas as pd

pd.options.display.max_rows = 101
pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 20

df = pd.read_csv('../data/file4.csv')

if __name__ == '__main__':
  print(df)
  # print(df.loc["day2"]) # error
  print(f'Pandas version: {pd.__version__}')

  # os.mkdir('../newdata/')
  # os.mkdir('../storedata/')

  # df.to_csv('../newdata/file4_editado.csv', header=True, index=False)
  # shutil.copy("../data/file1.csv", "../newdata/file1_copy.csv")
  # shutil.copy("../data/file2.csv", "../newdata/file2_copy.csv")
  # shutil.copy("../data/file3.csv", "../newdata/file3_copy.csv")
  #
  contenido = os.listdir('../newdata')
  print(contenido)

  for file in contenido:
    print(f'{file} detected in newdata folder')
    shutil.move(f'../newdata/{file}', f'../storedata/{file}')
    print(f'{file} moved to storedata')


