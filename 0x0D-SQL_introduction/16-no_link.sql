-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server where name is not null
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL AND `name` != ''
ORDER BY `score` DESC;
