import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)



if __name__ == '__main__':
  print(myvar)
  # print(myvar[0]) # error
  print(pd.__version__)
  