import os
import pandas as pd

csv_path = 'output/cleaned_ecommerce.csv'

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"File not found: {csv_path}\nCurrent directory: {os.getcwd()}")

df = pd.read_csv(csv_path, parse_dates=['InvoiceDate'])
print(df.head())

import sqlite3
conn = sqlite3.connect('output/ecommerce.db')
df.to_sql('sales', conn, index=False, if_exists='replace')
print('[OK] Data loaded to SQLite!')
conn.close()
