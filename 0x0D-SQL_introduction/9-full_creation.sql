 -- displays number of records with id of 89
CREATE table IF NOT EXISTS second_table(`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(256),
`score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (NULL, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (NULL, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (NULL, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (NULL, 'George', 8);
