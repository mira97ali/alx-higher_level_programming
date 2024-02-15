-- Ensure the table id_not_null does not already exist before creation
-- Then create table with id INT defaulting to 1 and name as VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
