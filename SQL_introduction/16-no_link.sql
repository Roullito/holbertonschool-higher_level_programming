-- Lists records from second_table where name is not empty, ordered by score descending
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
