-- List all genres associated with the show Dexter from the hbtn_0d_tvshows database
-- Then sort the results by genre name in ascending order
-- Finnaly Utilize a JOIN operation to connect the tv_shows, tv_show_genres, and tv_genres tables based on matching conditions
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
