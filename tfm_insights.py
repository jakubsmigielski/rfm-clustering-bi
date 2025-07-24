import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


rfm = pd.read_csv('../output/rfm_scores.csv')

print("==== RFM Dataset Preview ====")
print(rfm.head())
print("\nColumns:", rfm.columns)
print("\nNull values:\n", rfm.isnull().sum())


plt.figure(figsize=(8, 5))
sns.histplot(rfm['RFM_Score'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of RFM_Score')
plt.xlabel('RFM_Score')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()


top_segments = rfm['RFM_Segment'].value_counts().head(5)
print("\nTop 5 most common RFM segments:")
print(top_segments)


segment_map = {
    'Champions': [444, 344, 443, 433, 334],
    'Loyal Customers': [333, 334, 343, 344], }



print("\nRFM_Score statistics:\n", rfm['RFM_Score'].describe())


plt.figure(figsize=(6,4))
sns.heatmap(rfm[['Recency','Frequency','Monetary']].corr(), annot=True, cmap='Blues')
plt.title('Correlation between R, F, M')
plt.tight_layout()
plt.show()


pivot = pd.pivot_table(rfm, index='R_quartile', columns='F_quartile', values='CustomerID', aggfunc='count')
print("\nPivot table: Recency vs Frequency quartiles (customer count):")
print(pivot)


print("\n==== Key Insights ====")
print(f"Total customers analyzed: {rfm['CustomerID'].nunique()}")
print(f"Largest segment: {top_segments.idxmax()} with {top_segments.max()} customers.")
print("Distribution of RFM_Score suggests (describe histogram shape).")
print("Correlation matrix shows which variables are related.")


top_seg_customers = rfm[rfm['RFM_Segment'] == top_segments.idxmax()]
top_seg_customers.to_csv('../output/top_segment_customers.csv', index=False)

