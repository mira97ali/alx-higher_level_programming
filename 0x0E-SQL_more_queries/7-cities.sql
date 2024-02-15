-- Ensure the database hbtn_0d_usa exists
-- Select the database hbtn_0d_usa for use
-- Create the table states if it does not exist to ensure foreign key constraint can be applied
-- Create the table cities with the specified requirements and a foreign key that references the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);
