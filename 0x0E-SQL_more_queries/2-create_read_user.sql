-- Check if the database hbtn_0d_2 already exists and create it if not
-- Then create the user user_0d_2 with password user_0d_2_pwd if it does not already exist
-- Then grant SELECT privilege on hbtn_0d_2 database to user_0d_2
-- Finally apply the privilege changes
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
