-- This script lists all shows from hbtn_0d_tvshows_rate by their rating sum
-- Each record displays the show title and its total rating
-- Results are sorted in descending order by the rating
SELECT s.title, SUM(r.rating) AS rating_sum
FROM tv_shows AS s
JOIN tv_show_ratings AS r ON s.id = r.show_id
GROUP BY s.id
ORDER BY rating_sum DESC, s.title ASC;
