import pandas as pd

rfm = pd.read_csv('../output/cleaned_ecommerce.csv', parse_dates=['InvoiceDate'])

snapshot_date = rfm['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm_table = rfm.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'count',                                     # Frequency
    'TotalPrice': 'sum'                                       # Monetary
}).reset_index()

rfm_table.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)


rfm_table['R_quartile'] = pd.qcut(rfm_table['Recency'], 4, labels=[4, 3, 2, 1])
rfm_table['F_quartile'] = pd.qcut(rfm_table['Frequency'], 4, labels=[1, 2, 3, 4])
rfm_table['M_quartile'] = pd.qcut(rfm_table['Monetary'], 4, labels=[1, 2, 3, 4])

rfm_table['RFM_Segment'] = rfm_table['R_quartile'].astype(str) + rfm_table['F_quartile'].astype(str) + rfm_table['M_quartile'].astype(str)
rfm_table['RFM_Score'] = rfm_table[['R_quartile', 'F_quartile', 'M_quartile']].astype(int).sum(axis=1)

rfm_table.to_csv('../output/rfm_scores.csv', index=False)
print("[OK] rfm_scores.csv saved to ../output/")
