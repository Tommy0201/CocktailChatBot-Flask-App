import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with your file paths
file1_path = 'recommend_sys/robust_cocktail_2.csv'
file2_path = 'recommend_sys/robust_cocktail_3.csv'

# Read CSV files into pandas DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df1 = df1.reset_index(drop=True)
df2 = df2.reset_index(drop=True)

# Compare DataFrames
res = df1.compare(df2)

print(res)
print("Differences in Index:", df1.index.difference(df2.index))
print("Differences in Columns:", df1.columns.difference(df2.columns))
