-- Retrieves records from `second_table` where `name` is not empty, sorted by `score` in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
