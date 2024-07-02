-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema chores_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `chores_db` ;

-- -----------------------------------------------------
-- Schema chores_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `chores_db` DEFAULT CHARACTER SET utf8mb3 ;
-- -----------------------------------------------------
-- Schema chores_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `chores_db` ;

-- -----------------------------------------------------
-- Schema chores_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `chores_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `chores_db` ;
USE `chores_db` ;

-- -----------------------------------------------------
-- Table `chores_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chores_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `chores_db`.`chores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chores_db`.`chores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `description` TEXT NOT NULL,
  `location` TEXT NOT NULL,
  `date` DATE NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_chores_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_chores_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `chores_db`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
