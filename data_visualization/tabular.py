import pandas as pd
alcohol_data = pd.read_csv( 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' )

print(alcohol_data.head())
print(alcohol_data.tail())