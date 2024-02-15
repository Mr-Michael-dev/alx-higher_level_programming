-- FILE: convert database to UTF8
-- Use ALTER query to convert database
ALTER DATABASE hbtn_0c_0 
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Use ALTER query to convert table
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- To convert the field:
ALTER TABLE first_table
MODIFY name VARCHAR(255)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
