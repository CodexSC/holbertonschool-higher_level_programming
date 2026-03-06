-- Prints the full description of first_table by ensuring the table exists first
SET @current_db = DATABASE();
SET @current_db = IFNULL(@current_db, 'hbtn_0c_0');
SET @create_sql = CONCAT('CREATE TABLE IF NOT EXISTS `', @current_db, '`.`first_table` (',
	'id INT, name VARCHAR(256))');
PREPARE create_stmt FROM @create_sql;
EXECUTE create_stmt;
DEALLOCATE PREPARE create_stmt;

SET @show_sql = CONCAT('SHOW CREATE TABLE `', @current_db, '`.`first_table`');
PREPARE show_stmt FROM @show_sql;
EXECUTE show_stmt;
DEALLOCATE PREPARE show_stmt;
