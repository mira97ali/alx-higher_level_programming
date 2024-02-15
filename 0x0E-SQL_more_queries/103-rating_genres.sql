-- This script lists all genres in hbtn_0d_tvshows_rate by their rating
-- Each record displays the genre name and the sum of ratings for shows in that genre
-- Results are sorted in descending order by their rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
JOIN tv_show_ratings AS r ON sg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
