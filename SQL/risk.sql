DROP TABLE IF EXISTS `aretes`;
CREATE TABLE IF NOT EXISTS `aretes` (
  `id_case1` int NOT NULL,
  `id_case2` int NOT NULL,
  KEY `id_case1` (`id_case1`),
  KEY `id_case2` (`id_case2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `cases`;
CREATE TABLE IF NOT EXISTS `cases` (
  `id_case` int NOT NULL AUTO_INCREMENT,
  `id_plateau` int NOT NULL,
  `id_continent` int NOT NULL,
  `x` int NOT NULL,
  `y` int NOT NULL,
  `svg` text NOT NULL,
  PRIMARY KEY (`id_case`),
  KEY `id_continent` (`id_continent`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `continents`;
CREATE TABLE IF NOT EXISTS `continents` (
  `id_plateau` int NOT NULL,
  `id_continent` int NOT NULL AUTO_INCREMENT,
  `nom_continent` int NOT NULL,
  `nb_pions` int NOT NULL,
  PRIMARY KEY (`id_continent`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `etat_partie`;
CREATE TABLE IF NOT EXISTS `etat_partie` (
  `id_partie` int NOT NULL,
  `id_cases` int NOT NULL,
  `id_joueur` int NOT NULL,
  `nb_pion` int NOT NULL,
  KEY `id_cases` (`id_cases`),
  KEY `id_joueur` (`id_joueur`),
  KEY `id_partie` (`id_partie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `joueurs`;
CREATE TABLE IF NOT EXISTS `joueurs` (
  `id_joueur` int NOT NULL AUTO_INCREMENT,
  `pseudo` int NOT NULL,
  `mdp` varchar(20) NOT NULL,
  PRIMARY KEY (`id_joueur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `joueurs_parties`;
CREATE TABLE IF NOT EXISTS `joueurs_parties` (
  `id_partie` int NOT NULL,
  `id_joueursuivant` int NOT NULL,
  `id_joueur` int NOT NULL,
  `resultat` text NOT NULL,
  KEY `id_partie` (`id_partie`),
  KEY `id_joueur` (`id_joueur`),
  KEY `id_joueursuivant` (`id_joueursuivant`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `parties`;
CREATE TABLE IF NOT EXISTS `parties` (
  `id_partie` int NOT NULL AUTO_INCREMENT,
  `id_plateau` int NOT NULL,
  `etat` tinyint(1) NOT NULL DEFAULT '0',
  `tour` int NOT NULL,
  PRIMARY KEY (`id_partie`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `plateaux`;
CREATE TABLE IF NOT EXISTS `plateaux` (
  `id_plateau` int NOT NULL AUTO_INCREMENT,
  `nom_plateau` varchar(30) NOT NULL,
  `image` text NOT NULL,
  PRIMARY KEY (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `tokens`;
CREATE TABLE IF NOT EXISTS `tokens` (
  `id_joueur` int NOT NULL,
  `token` int NOT NULL,
  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `aretes`
  ADD CONSTRAINT `aretes_ibfk_1` FOREIGN KEY (`id_case1`) REFERENCES `cases` (`id_case`),
  ADD CONSTRAINT `aretes_ibfk_2` FOREIGN KEY (`id_case2`) REFERENCES `cases` (`id_case`);

ALTER TABLE `cases`
  ADD CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`id_continent`) REFERENCES `continents` (`id_continent`),
  ADD CONSTRAINT `cases_ibfk_2` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

ALTER TABLE `continents`
  ADD CONSTRAINT `continents_ibfk_1` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

ALTER TABLE `etat_partie`
  ADD CONSTRAINT `etat_partie_ibfk_1` FOREIGN KEY (`id_cases`) REFERENCES `cases` (`id_case`),
  ADD CONSTRAINT `etat_partie_ibfk_2` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`),
  ADD CONSTRAINT `etat_partie_ibfk_3` FOREIGN KEY (`id_partie`) REFERENCES `parties` (`id_partie`);

ALTER TABLE `joueurs_parties`
  ADD CONSTRAINT `joueurs_parties_ibfk_1` FOREIGN KEY (`id_partie`) REFERENCES `parties` (`id_partie`),
  ADD CONSTRAINT `joueurs_parties_ibfk_2` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`),
  ADD CONSTRAINT `joueurs_parties_ibfk_3` FOREIGN KEY (`id_joueursuivant`) REFERENCES `joueurs` (`id_joueur`);

ALTER TABLE `parties`
  ADD CONSTRAINT `parties_ibfk_1` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

ALTER TABLE `token`
  ADD CONSTRAINT `token_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`);
COMMIT;
