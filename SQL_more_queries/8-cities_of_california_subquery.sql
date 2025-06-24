-- Lists all cities of California in hbtn_0d_usa ordered by cities.id ascending (no JOIN)
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
