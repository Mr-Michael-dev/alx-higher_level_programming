-- script to list all cities of California without using JOIN

-- query to list all cities of California sorted by cities.id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states
	WHERE name = 'California')
ORDER BY id ASC;
