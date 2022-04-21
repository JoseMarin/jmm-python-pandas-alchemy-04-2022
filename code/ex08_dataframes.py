import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])


if __name__ == '__main__':
  print(df)
  # print(df.loc["day2"]) # error
  print(pd.__version__)
  