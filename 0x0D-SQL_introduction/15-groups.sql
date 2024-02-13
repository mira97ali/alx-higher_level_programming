-- Groups records in `second_table` by score and counts the occurrences, sorted by count in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
