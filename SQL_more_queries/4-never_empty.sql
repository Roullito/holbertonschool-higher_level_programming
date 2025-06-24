-- Creates table id_not_null with id defaulting to 1 if not provided
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
