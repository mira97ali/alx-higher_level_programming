-- This script lists all TV shows that are not categorized under the genre "Comedy"
-- Results are sorted in ascending order by the show title
SELECT s.title 
FROM tv_shows AS s 
WHERE s.id NOT IN (
    -- Subquery to identify shows with the "Comedy" genre
    SELECT sg.show_id 
    FROM tv_show_genres AS sg 
    JOIN tv_genres AS g ON sg.genre_id = g.id 
    WHERE g.name = 'Comedy'
) 
ORDER BY s.title ASC;
