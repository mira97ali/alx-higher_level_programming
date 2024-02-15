-- List all shows from the hbtn_0d_tvshows database that do not have a genre linked
-- Then each record will display tv_shows.title and a NULL value for tv_show_genres.genre_id
-- Then results are sorted in ascending order by tv_shows.title
-- Finally this query uses a LEFT JOIN to include shows and filters out those with a genre using a WHERE clause checking for NULL genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title;
