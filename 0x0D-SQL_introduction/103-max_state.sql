-- FILE: script to display top 3 state with max temperature all records
-- using SELECT, AVG() and LIMIT
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;
