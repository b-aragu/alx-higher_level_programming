-- a script that updates the score of Bob to 10 in the table second_table
-- You are not allowed to use Bob’s id value, only the name field
SELECT
    tv_shows.title,
    IFNULL(tv_show_genres.genre_id, 'No Genre') AS genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE
    tv_show_genres.genre_id IS NULL
ORDER BY
    tv_shows.title ASC, tv_show_genres.genre_id ASC;

