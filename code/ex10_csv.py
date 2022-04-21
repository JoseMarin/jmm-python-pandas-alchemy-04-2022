import pandas as pd
import matplotlib.pyplot as plt

# list of name, degree, score
nme = ["Jose Luís", "Diana", "David", "Geek"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [40, 100, 67, 78]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('../data/file2.csv', header=False, index=False)

if __name__ == '__main__':
  print(df)
  print(pd.__version__)

  df.plot(kind="barh", x='name')

  plt.show()
  