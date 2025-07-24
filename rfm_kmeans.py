import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


rfm = pd.read_csv('../output/rfm_scores.csv')

features = ['Recency', 'Frequency', 'Monetary']
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[features])


wcss = []
K_range = range(2, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(K_range, wcss, marker='o')
plt.title('Elbow Method: Choose Optimal Number of Clusters')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS (inertia)')
plt.tight_layout()
plt.show()

k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

cluster_stats = rfm.groupby('Cluster')[features].mean().round(2)
print("\nAverage RFM values per cluster:")
print(cluster_stats)

print("\nNumber of customers per cluster:")
print(rfm['Cluster'].value_counts())

rfm[['CustomerID', 'Cluster']].to_csv('../output/rfm_clusters.csv', index=False)
print("\nClusters exported to ../output/rfm_clusters.csv")
