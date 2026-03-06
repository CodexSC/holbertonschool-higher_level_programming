-- Lists all tables of the current or fallback database
SET @current_db = DATABASE();
SET @current_db = IFNULL(@current_db, 'hbtn_0c_0');
SET @sql = CONCAT('SHOW TABLES FROM `', @current_db, '`');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
