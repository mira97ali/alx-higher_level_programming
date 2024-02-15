-- List all Comedy shows from the hbtn_0d_tvshows database
-- Then sort the results by show title in ascending order
-- Finally utilize a JOIN operation to connect the tv_shows, tv_show_genres, and tv_genres tables based on matching conditions
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
