-- List all cities along with their corresponding state name using a subquery for state name matching
SELECT c.id, c.name, (SELECT s.name FROM states AS s WHERE s.id = c.state_id) AS state_name
FROM cities AS c
ORDER BY c.id ASC;
