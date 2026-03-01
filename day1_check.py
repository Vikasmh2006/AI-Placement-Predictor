import pandas as pd

data = pd.read_csv("placement.csv")

print(data.head())

print("\nColumns in Dataset:\n")
print(data.columns)