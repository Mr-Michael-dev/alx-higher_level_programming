-- FILE: script to list all records with score >= 10 in a table
-- using SELECT to list rows and WHERE for condition
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
