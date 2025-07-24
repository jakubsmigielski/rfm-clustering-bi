import sqlite3
import pandas as pd

# 1. Open connection
conn = sqlite3.connect('../output/ecommerce.db')

# 2. Total sales per country
query1 = """
SELECT Country, SUM(TotalPrice) AS TotalSales
FROM sales
GROUP BY Country
ORDER BY TotalSales DESC
"""
sales_by_country = pd.read_sql_query(query1, conn)
print("Total sales per country:\n", sales_by_country.head())

# 3. Top 5 customers by total spend
query2 = """
SELECT CustomerID, SUM(TotalPrice) AS TotalSpend
FROM sales
GROUP BY CustomerID
ORDER BY TotalSpend DESC
LIMIT 5
"""
top_customers = pd.read_sql_query(query2, conn)
print("\nTop 5 customers by total spend:\n", top_customers)

# 4. Monthly sales trend
query3 = """
SELECT strftime('%Y-%m', InvoiceDate) AS YearMonth, SUM(TotalPrice) AS MonthlySales
FROM sales
GROUP BY YearMonth
ORDER BY YearMonth
"""
monthly_sales = pd.read_sql_query(query3, conn)
print("\nMonthly sales trend:\n", monthly_sales.head())

# 5. Most popular products (by quantity sold)
query4 = """
SELECT Description, SUM(Quantity) AS TotalQuantity
FROM sales
GROUP BY Description
ORDER BY TotalQuantity DESC
LIMIT 10
"""
top_products = pd.read_sql_query(query4, conn)
print("\nTop 10 most popular products:\n", top_products)

# 6. Average order value by country
query5 = """
SELECT Country, AVG(TotalPrice) AS AvgOrderValue
FROM sales
GROUP BY Country
ORDER BY AvgOrderValue DESC
"""
avg_order_value = pd.read_sql_query(query5, conn)
print("\nAverage order value by country:\n", avg_order_value.head())

# 7. Number of orders per customer
query6 = """
SELECT CustomerID, COUNT(DISTINCT InvoiceNo) AS NumOrders
FROM sales
GROUP BY CustomerID
ORDER BY NumOrders DESC
LIMIT 10
"""
orders_per_customer = pd.read_sql_query(query6, conn)
print("\nTop 10 customers by number of orders:\n", orders_per_customer)

# 8. Repeat customers (customers with > 1 order)
query7 = """
SELECT COUNT(*) AS RepeatCustomers
FROM (
    SELECT CustomerID
    FROM sales
    GROUP BY CustomerID
    HAVING COUNT(DISTINCT InvoiceNo) > 1
) sub
"""
repeat_customers = pd.read_sql_query(query7, conn)
print("\nNumber of repeat customers:", repeat_customers.iloc[0, 0])

# 9. Sales on each weekday
query8 = """
SELECT strftime('%w', InvoiceDate) AS Weekday, SUM(TotalPrice) AS Sales
FROM sales
GROUP BY Weekday
ORDER BY Weekday
"""
weekday_sales = pd.read_sql_query(query8, conn)
print("\nSales by weekday (0=Sunday, 6=Saturday):\n", weekday_sales)

# 10. Anomalous transactions (returns/corrections)
query9 = """
SELECT *
FROM sales
WHERE Quantity < 0 OR UnitPrice < 0 OR TotalPrice < 0
LIMIT 10
"""
anomalies = pd.read_sql_query(query9, conn)
print("\nExample of anomalous transactions (returns/corrections):\n", anomalies)

import sqlite3
import pandas as pd

conn = sqlite3.connect('../output/ecommerce.db')

# CLV: Customer Lifetime Value
query_clv = """
SELECT CustomerID, ROUND(SUM(TotalPrice),2) AS CLV
FROM sales
GROUP BY CustomerID
ORDER BY CLV DESC
"""
clv = pd.read_sql_query(query_clv, conn)
print("\nTop 10 customers by CLV:")
print(clv.head(10))

# Histogram of CLV
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
plt.hist(clv['CLV'], bins=50, color='teal', edgecolor='black')
plt.title('Distribution of Customer Lifetime Value')
plt.xlabel('CLV')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

# Basic stats
print("\nCLV - basic statistics:\n", clv['CLV'].describe())

conn.close()



