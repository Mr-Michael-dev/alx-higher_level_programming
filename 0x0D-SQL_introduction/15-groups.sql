-- FILE: count number of records with the same score
-- using COUNT and where queries to count same score
SELECT score, COUNT(score) AS number
FROM second_table
-- group the set by score
GROUP BY score
ORDER BY score DESC;
