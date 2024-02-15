-- List all genres from the hbtn_0d_tvshows database and the number of shows linked to each
-- Then only display genres with at least one show linked and sort the results by the number of linked shows in descending order
-- Then use RIGHT JOIN to include all entries from tv_show_genres and matching entries from tv_genres
-- Finally count the number of shows linked to each genre, grouping the results by genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres 
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
