import pandas as pd
from datetime import timedelta

df = pd.read_csv('../output/cleaned_ecommerce.csv', parse_dates=['InvoiceDate'])

max_date = df['InvoiceDate'].max()
cutoff = max_date - timedelta(days=30)

features = df[df['InvoiceDate'] <= cutoff].copy()

rfm = features.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (cutoff - x.max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
}).rename(columns={'InvoiceDate':'Recency', 'InvoiceNo':'Frequency', 'TotalPrice':'Monetary'}).reset_index()

after_cutoff = df[df['InvoiceDate'] > cutoff]
rfm['Target'] = rfm['CustomerID'].isin(after_cutoff['CustomerID']).astype(int)

print(rfm.head())
rfm.to_csv('../output/rfm_ml.csv', index=False)