import pandas as pd

df = pd.read_excel('../data/Online Retail.xlsx')

df = df.dropna(subset=['Description', 'CustomerID'])

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

df = df.drop_duplicates()

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print(f'Number of records after cleaning: {len(df)}')
print(df.head())

df.to_csv('../output/cleaned_ecommerce.csv', index=False)
