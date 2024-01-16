-- Script to prepare a MySQL server for project database being hbnb_dev_db
-- With new user hbnh_dev (in localhost) password being set to hbnb_dev_pwd
-- hbnb should have privileges on the database
-- hbnb should have SELECT privilege on database 'performance_schema'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
