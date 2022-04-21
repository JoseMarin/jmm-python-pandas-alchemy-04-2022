import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)



if __name__ == '__main__':
  print(myvar)

  # refer to the row index:
  print(myvar.loc[0])

  # use a list of indexes:
  print(myvar.loc[[0, 1]])

  print(pd.__version__)
  