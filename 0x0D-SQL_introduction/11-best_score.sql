-- Selects entries from `second_table` with scores of 10 or higher, sorted by score in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
