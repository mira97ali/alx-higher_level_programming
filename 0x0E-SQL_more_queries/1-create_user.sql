-- Check if user 'user_0d_1' exists and create it with a password if it does not
-- Then grant all privileges to 'user_0d_1' on all databases and tables
-- Finally apply the changes made by the GRANT statement
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
