import pandas as pd
import sqlite3
import os


OUTPUT_DIR = '../output/'
DB_PATH = os.path.join(OUTPUT_DIR, 'ecommerce.db')

csv_tables = [
    ('cleaned_ecommerce.csv', 'sales'),
    ('rfm_scores.csv', 'rfm'),
    ('rfm_ml.csv', 'rfm_ml')
]

conn = sqlite3.connect(DB_PATH)

for csv_file, table_name in csv_tables:
    csv_path = os.path.join(OUTPUT_DIR, csv_file)
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, index=False, if_exists='replace')
        print(f"[OK] {csv_file} loaded into table '{table_name}'")
    else:
        print(f"[SKIPPED] File not found: {csv_file}")

conn.close()
print("\nAll tables successfully loaded into ecommerce.db!")


