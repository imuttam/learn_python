import pandas as pd

print(pd.__version__)

data = r'../report.csv'

df = pd.read_csv(data)
# print(df.shape())
print(df.head())
print(df.columns)
print(df.info())

print(df.value_counts())
