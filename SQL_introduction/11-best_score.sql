-- Lists records with score >= 10 from second_table ordered by top score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
