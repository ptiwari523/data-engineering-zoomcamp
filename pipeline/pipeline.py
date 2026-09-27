import sys
import pandas as pd

print('arguments', sys.argv)
month = int(sys.argv[1])

data = {"day": [1,2], "number_passangers": [3,4]}
df = pd.DataFrame(data)
df['month'] = month
df.to_parquet(f"output_{month}.parquet")

print(df.head())

# print(f"Hello pipeline, month is: {month}")