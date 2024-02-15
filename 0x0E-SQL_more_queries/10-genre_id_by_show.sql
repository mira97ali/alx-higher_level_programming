-- List all shows from the hbtn_0d_tvshows database that have at least one genre linked
-- Then each record will display tv_shows.title and tv_show_genres.genre_id
-- Then results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Then this query utilizes a JOIN between the tv_shows and tv_show_genres tables
-- Finally the condition for the JOIN is the matching of tv_shows.id with tv_show_genres.show_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
