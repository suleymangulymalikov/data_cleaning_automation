import pandas as pd

file_name = "data.csv"

df = pd.read_csv(file_name)

print(df.head())