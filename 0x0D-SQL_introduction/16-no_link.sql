-- FILE: script to list all records in a table
-- dont list rows without a name value
-- using SELECT to list rows
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
