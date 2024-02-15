-- This script selects genres not linked to the TV show "Dexter"
-- It sorts the results in ascending order by genre name
SELECT g.name 
FROM tv_genres AS g 
WHERE g.id NOT IN (
    -- Subquery to find genres linked to "Dexter"
    SELECT sg.genre_id 
    FROM tv_show_genres AS sg 
    JOIN tv_shows AS s ON sg.show_id = s.id 
    WHERE s.title = 'Dexter'
) 
ORDER BY g.name ASC;
