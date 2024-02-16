-- script that creates a database and new user
-- user should have SELECT priviledge in the database

-- use CREATE DATABASE TO create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- use CREATE USER to create new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- use GRANT to grant priviledges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
