-- script that creates a database and a table

-- use CREATE DATABASE TO create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to the newly created or existing database
USE hbtn_0d_usa;

-- use CREATE TABLE to create table with unique auogenerated id and id has primary key
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT NOT NULL,
	-- create a foreign key constraint
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
