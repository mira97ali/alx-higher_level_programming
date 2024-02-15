-- List all genres from the hbtn_0d_tvshows database and count the number of shows linked to each genre
-- Then each record will display the genre and the number of shows linked to that genre
-- Then genres without any shows linked will not be displayed
-- Then results are sorted in descending order by the number of shows linked
-- Finally this query utilizes INNER JOIN to ensure only genres with linked shows are counted and GROUP BY to aggregate results by genre
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
