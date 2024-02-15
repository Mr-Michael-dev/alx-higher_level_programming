-- FILE: script to compute the temperature average of all records
-- using SELECT AVG()
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
