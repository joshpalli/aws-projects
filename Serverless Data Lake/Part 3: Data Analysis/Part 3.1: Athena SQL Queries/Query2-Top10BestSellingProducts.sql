-- Top 10 Best Selling Products
SELECT productname, SUM(price) AS sales 
FROM raw
GROUP BY productname
ORDER BY sales desc
LIMIT 10