-- This script lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record displays the show title and the sum of its ratings
-- Results are sorted in descending order by the rating
SELECT title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
