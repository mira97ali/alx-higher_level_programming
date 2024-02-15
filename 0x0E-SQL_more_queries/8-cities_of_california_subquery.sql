-- Select all cities from California without using JOIN, using a subquery to find the state_id for California
SELECT c.id, c.name FROM cities AS c
WHERE c.state_id = (
  SELECT s.id FROM states AS s WHERE s.name = 'California'
)
ORDER BY c.id ASC;
