-- script that creates a new user
-- use CREATE USER to create
CREATE IF NOT EXISTS USER 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
