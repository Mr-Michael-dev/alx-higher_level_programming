-- FILE: script to display top 3 cities temperature average of all records
-- using SELECT, AVG() and LIMIT
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
