

-- Food Table --
CREATE  TABLE `hungryy-db`.`food` (
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `description` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) );

-- Ingredient Table --
CREATE  TABLE `hungryy-db`.`ingredient` (
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) );

-- Food_Ingredient --
CREATE  TABLE `hungryy-db`.`food_ingredient` (
  `food_id` BIGINT NOT NULL ,
  `ingredient_id` BIGINT NOT NULL ,
  PRIMARY KEY (`food_id`, `ingredient_id`) ,
  INDEX `fk_food_id` (`food_id` ASC) ,
  INDEX `fk_ingredient_id` (`ingredient_id` ASC) ,
  CONSTRAINT `fk_food_id`
    FOREIGN KEY (`food_id` )
    REFERENCES `hungryy-db`.`food` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingredient_id`
    FOREIGN KEY (`ingredient_id` )
    REFERENCES `hungryy-db`.`ingredient` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
