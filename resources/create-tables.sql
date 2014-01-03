

-- recipe table --
CREATE  TABLE `hungryy-db`.`recipe` (
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `description` VARCHAR(45) NULL ,
  `preparation_time` VARCHAR(45) NULL ,
  `portion` VARCHAR(45) NULL,
  `caloric_information` VARCHAR(45) NULL,
  PRIMARY KEY (`id`) );

-- ingredient table --
CREATE  TABLE `hungryy-db`.`ingredient` (
  `id` BIGINT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) );

-- recipe_ingredient table --
CREATE  TABLE `hungryy-db`.`recipe_ingredient` (
  `recipe_id` BIGINT NOT NULL ,
  `ingredient_id` BIGINT NOT NULL ,
  `ingredient_text` VARCHAR(140) NOT NULL,
  PRIMARY KEY (`recipe_id`, `ingredient_id`) ,
  INDEX `fk_recipe_id` (`recipe_id` ASC) ,
  INDEX `fk_ingredient_id` (`ingredient_id` ASC) ,
  CONSTRAINT `fk_recipe_id`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `hungryy-db`.`recipe` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingredient_id`
    FOREIGN KEY (`ingredient_id` )
    REFERENCES `hungryy-db`.`ingredient` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- category table--
CREATE  TABLE `hungryy-db`.`category` (
  `id` BIGINT NOT NULL ,
  `Name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) );

-- recipe_category table--
CREATE  TABLE `hungryy-db`.`recipe_category` (
  `recipe_id` BIGINT NOT NULL ,
  `category_id` BIGINT NOT NULL ,
  PRIMARY KEY (`recipe_id`, `category_id`) ,
  INDEX `fk_recipe_id` (`recipe_id` ASC) ,
  INDEX `fk_category_id` (`category_id` ASC) ,
  CONSTRAINT `fk_recipe_id`
    FOREIGN KEY (`recipe_id` )
    REFERENCES `hungryy-db`.`recipe` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_category_id`
    FOREIGN KEY (`category_id` )
    REFERENCES `hungryy-db`.`category` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
