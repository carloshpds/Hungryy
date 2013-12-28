
-- Mockup Foods  --
INSERT INTO `hungryy-db`.`food` (`id`, `name`, `description`) VALUES (1, 'Hot Dog', 'Pao com salsicha');
INSERT INTO `hungryy-db`.`food` (`id`, `name`, `description`) VALUES (2, 'Misto Quente', 'Pao com presunto e queijo na chapa');
INSERT INTO `hungryy-db`.`food` (`id`, `name`, `description`) VALUES (3, 'Hamburguer', 'Tradicional pao com hamburguer');


-- Mockup Ingredients --
INSERT INTO `hungryy-db`.`ingredient` (`id`, `name`) VALUES (1, 'Queijo');
INSERT INTO `hungryy-db`.`ingredient` (`id`, `name`) VALUES (2, 'Presunto');
INSERT INTO `hungryy-db`.`ingredient` (`id`, `name`) VALUES (3, 'Pao');
INSERT INTO `hungryy-db`.`ingredient` (`id`, `name`) VALUES (4, 'Salsicha');
INSERT INTO `hungryy-db`.`ingredient` (`id`, `name`) VALUES (5, 'Hamburguer');


-- Mockup Food_Ingredient --
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (1, 3);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (1, 4);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (2, 1);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (2, 2);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (2, 3);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (3, 3);
INSERT INTO `hungryy-db`.`food_ingredient` (`food_id`, `ingredient_id`) VALUES (3, 5);

