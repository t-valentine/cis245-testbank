-- -----------------------------------------------------
-- Schema testbank
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testbank` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `testbank` ;

-- -----------------------------------------------------
-- Table `testbank`.`questions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`questions` (
  `qstn_id` INT NOT NULL,
  `qstn_description` VARCHAR(300) NULL DEFAULT NULL,
  `qstn_answer` INT NULL DEFAULT NULL,
  PRIMARY KEY (`qstn_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `testbank`.`answers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`answers` (
  `ans_id` INT NOT NULL,
  `ans_description` VARCHAR(300) NULL DEFAULT NULL,
  `ans_right` CHAR(1) NULL DEFAULT NULL,
  `questions_qstn_id` INT NOT NULL,
  PRIMARY KEY (`ans_id`, `questions_qstn_id`),
  INDEX `fk_answers_questions1_idx` (`questions_qstn_id` ASC) VISIBLE,
  CONSTRAINT `fk_answers_questions1`
    FOREIGN KEY (`questions_qstn_id`)
    REFERENCES `testbank`.`questions` (`qstn_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `testbank`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`category` (
  `category_id` INT NOT NULL,
  `category_desc` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `testbank`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`users` (
  `user_id` INT NOT NULL,
  `user_name` VARCHAR(20) NULL DEFAULT NULL,
  `user_password` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `testbank`.`tests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`tests` (
  `test_id` INT NOT NULL,
  `test_date` DATETIME NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `qstn_id` INT NULL DEFAULT NULL,
  `users_user_id` INT NOT NULL,
  PRIMARY KEY (`test_id`, `users_user_id`),
  INDEX `fk_tests_users_idx` (`users_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tests_users`
    FOREIGN KEY (`users_user_id`)
    REFERENCES `testbank`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `testbank`.`tests_questions_rel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbank`.`tests_questions_rel` (
  `questions_qstn_id` INT NOT NULL,
  `tests_test_id` INT NOT NULL,
  `tests_users_user_id` INT NOT NULL,
  `category_category_id` INT NOT NULL,
  PRIMARY KEY (`questions_qstn_id`, `tests_test_id`, `tests_users_user_id`, `category_category_id`),
  INDEX `fk_questions_has_tests_tests1_idx` (`tests_test_id` ASC, `tests_users_user_id` ASC) VISIBLE,
  INDEX `fk_questions_has_tests_questions1_idx` (`questions_qstn_id` ASC) VISIBLE,
  INDEX `fk_questions_has_tests_category1_idx` (`category_category_id` ASC) VISIBLE,
  CONSTRAINT `fk_questions_has_tests_questions1`
    FOREIGN KEY (`questions_qstn_id`)
    REFERENCES `testbank`.`questions` (`qstn_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_questions_has_tests_tests1`
    FOREIGN KEY (`tests_test_id` , `tests_users_user_id`)
    REFERENCES `testbank`.`tests` (`test_id` , `users_user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_questions_has_tests_category1`
    FOREIGN KEY (`category_category_id`)
    REFERENCES `testbank`.`category` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;