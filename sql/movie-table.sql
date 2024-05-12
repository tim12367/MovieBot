CREATE TABLE `movie_bot`.`movie_info` (
  `film_title` VARCHAR(50) NOT NULL,
  `movie_length` VARCHAR(45) NULL,
  `release_date` DATE NULL,
  `create_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  `change_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`));
