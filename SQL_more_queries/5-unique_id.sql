-- Creates table unique_id with a UNIQUE id field defaulting to 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
