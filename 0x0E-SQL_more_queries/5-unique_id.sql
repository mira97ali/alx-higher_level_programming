
-- Check if the table unique_id already exists and create it if not
-- Then define id as INT with a default value of 1 and ensure it is unique
-- Finally define name as VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
