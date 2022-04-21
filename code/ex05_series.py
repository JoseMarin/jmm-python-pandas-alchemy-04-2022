import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])



if __name__ == '__main__':
  print(myvar)
  print(myvar["day2"])
  print(pd.__version__)
  