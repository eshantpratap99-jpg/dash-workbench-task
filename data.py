import pandas as pd
import glob
import os

# 1. Find all the CSV files in the data folder
data_files = glob.glob('data/*.csv')

# 2. Combine them into one list of dataframes
df_list = []
for file in data_files:
    df_list.append(pd.read_csv(file))

# 3. Merge all data into one big table
df = pd.concat(df_list)

# 4. Keep only 'pink morsel' rows (ignoring capitalization)
df = df[df['product'].str.lower() == 'pink morsel']

# 5. Create the 'sales' column by multiplying price and quantity
# First, clean the price column (remove '$' if present)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

# 6. Keep only the columns we need
df = df[['sales', 'date', 'region']]

# 7. Save the final formatted file
df.to_csv('formatted_data.csv', index=False)

print("Data processing complete! 'formatted_data.csv' has been created.")