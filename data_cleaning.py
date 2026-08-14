import pandas as pd

# 1. File load ki
df = pd.read_csv("sales_data.csv")

# 2. Check kia k kis column me kitni khali (Missing) values hain
print("--- Missing Values Report ---")
print(df.isnull().sum())

# 3. Missing values ko theek karna
# Agar 'Qty' me koi cell khali hai to wahan 0 likh dena
if 'Qty' in df.columns:
    df['Qty'] = df['Qty'].fillna(0)

# 4. Duplicate rows ko dhoond kar delete karna
duplicate_count = df.duplicated().sum()
print(f"\nTotal duplicate rows found: {duplicate_count}")
df = df.drop_duplicates()

# 5. Cleaned data ko nayi CSV file me save karna
df.to_csv("cleaned_sales_data.csv", index=False)
print("\n🎉 Success: Cleaned data save ho chuka hai!")
