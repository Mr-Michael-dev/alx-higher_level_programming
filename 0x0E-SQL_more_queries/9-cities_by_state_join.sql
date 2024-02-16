-- script to list all cities contained in hbtn_0d_usa

-- query to list all cities id and name by state sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
