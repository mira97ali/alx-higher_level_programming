-- List all shows from the hbtn_0d_tvshows database, including those without a genre
-- Then each record will display tv_shows.title and tv_show_genres.genre_id
-- Then results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Then shows without a genre will display NULL for the genre_id
-- Finally this query uses a LEFT JOIN to include shows that do not have a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
