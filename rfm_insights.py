import pandas as pd

rfm = pd.read_csv('../output/rfm_scores.csv')


print("Customers per RFM_Score:")
print(rfm['RFM_Score'].value_counts().sort_index())


print("\nAverage Monetary per RFM_Score:")
print(rfm.groupby('RFM_Score')['Monetary'].mean())


print("\nTop 10 customers by RFM_Score & Monetary:")
print(rfm.sort_values(['RFM_Score', 'Monetary'], ascending=[False, False]).head(10))


print("\nTop 5 RFM segments by size:")
print(rfm['RFM_Segment'].value_counts().head(5))


rfm_summary = rfm.pivot_table(index='R_quartile', columns='F_quartile', values='CustomerID', aggfunc='count')
print("\nPivot table R vs F (counts):")
print(rfm_summary)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.histplot(rfm['RFM_Score'], bins=8, kde=True)
plt.title('Distribution of RFM_Score')
plt.xlabel('RFM_Score')
plt.ylabel('Number of Customers')
plt.show()
