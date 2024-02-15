-- Select all cities and their corresponding state names from the database
-- Then each record will display cities.id, cities.name, and states.name
-- Then the results are sorted in ascending order by cities.id
-- Then this is achieved by performing a LEFT JOIN between the cities and states tables
-- Finally the JOIN condition is that the states.id matches cities.state_id
SELECT cities.id, cities.name, states.name 
FROM cities 
LEFT JOIN states ON states.id = cities.state_id 
ORDER BY cities.id;
