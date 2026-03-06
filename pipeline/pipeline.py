import sys 
print(f"arguments {sys.argv}")
month = int(sys.argv[1])
print(f'Running pipeline for {month}')


import pandas as pd 
df = pd.DataFrame ({"A":[1,2] , "B":[3,4]})
print(df.head())

df.to_parquet(f'output_{month}.parquet')


# import pandas as pd

# df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
# print(df.head())

# df.to_parquet(f"output_day_{sys.argv[1]}.parquet")