-- Check if the table force_name already exists in the database and create it if not
-- Then define id as INT and name as VARCHAR(256) which cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
