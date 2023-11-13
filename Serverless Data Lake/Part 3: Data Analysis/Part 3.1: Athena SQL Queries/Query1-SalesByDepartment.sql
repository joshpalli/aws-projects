-- Return the sales of each department in descending order
SELECT department, SUM(price) AS total_sales
FROM raw
GROUP BY department
ORDER BY department desc;