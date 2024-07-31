-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows
-- lists all rows of a database corresponding to a column value
SELECT title
FROM tv_shows
LEFT JOIN tv_genres ON tv_genres.id = tv_shows.id
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
