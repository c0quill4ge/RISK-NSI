-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3307
-- Généré le : ven. 02 juin 2023 à 06:44
-- Version du serveur : 10.6.5-MariaDB
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `risk`
--

-- --------------------------------------------------------

--
-- Structure de la table `aretes`
--

DROP TABLE IF EXISTS `aretes`;
CREATE TABLE IF NOT EXISTS `aretes` (
  `id_case1` int(11) NOT NULL,
  `id_case2` int(11) NOT NULL,
  KEY `id_case1` (`id_case1`),
  KEY `id_case2` (`id_case2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `cases`
--

DROP TABLE IF EXISTS `cases`;
CREATE TABLE IF NOT EXISTS `cases` (
  `id_case` int(11) NOT NULL AUTO_INCREMENT,
  `id_plateau` int(11) NOT NULL,
  `id_continent` int(11) NOT NULL,
  `nom_pays` text NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `svg` text NOT NULL,
  PRIMARY KEY (`id_case`),
  KEY `id_continent` (`id_continent`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `continents`
--

DROP TABLE IF EXISTS `continents`;
CREATE TABLE IF NOT EXISTS `continents` (
  `id_plateau` int(11) NOT NULL,
  `id_continent` int(11) NOT NULL AUTO_INCREMENT,
  `nom_continent` int(11) NOT NULL,
  `nb_pions` int(11) NOT NULL,
  PRIMARY KEY (`id_continent`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `etat_partie`
--

DROP TABLE IF EXISTS `etat_partie`;
CREATE TABLE IF NOT EXISTS `etat_partie` (
  `id_partie` int(11) NOT NULL,
  `id_cases` int(11) NOT NULL,
  `id_joueur` int(11) NOT NULL,
  `nb_pion` int(11) NOT NULL,
  KEY `id_cases` (`id_cases`),
  KEY `id_joueur` (`id_joueur`),
  KEY `id_partie` (`id_partie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `joueurs`
--

DROP TABLE IF EXISTS `joueurs`;
CREATE TABLE IF NOT EXISTS `joueurs` (
  `id_joueur` int(11) NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(13) NOT NULL,
  `mdp` TEXT NOT NULL,
  PRIMARY KEY (`id_joueur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `joueurs_parties`
--

DROP TABLE IF EXISTS `joueurs_parties`;
CREATE TABLE IF NOT EXISTS `joueurs_parties` (
  `id_partie` int(11) NOT NULL,
  `id_joueursuivant` int(11) NOT NULL,
  `id_joueur` int(11) NOT NULL,
  `resultat` text NOT NULL,
  KEY `id_partie` (`id_partie`),
  KEY `id_joueur` (`id_joueur`),
  KEY `id_joueursuivant` (`id_joueursuivant`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `parties`
--

DROP TABLE IF EXISTS `parties`;
CREATE TABLE IF NOT EXISTS `parties` (
  `id_partie` int(11) NOT NULL AUTO_INCREMENT,
  `id_plateau` int(11) NOT NULL,
  `tour` int(11) NOT NULL,
  `etat` enum('debut','en_cours','fin','') NOT NULL,
  PRIMARY KEY (`id_partie`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `plateaux`
--

DROP TABLE IF EXISTS `plateaux`;
CREATE TABLE IF NOT EXISTS `plateaux` (
  `id_plateau` int(11) NOT NULL AUTO_INCREMENT,
  `nom_plateau` varchar(30) NOT NULL,
  `image` text NOT NULL,
  PRIMARY KEY (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `tokens`
--

DROP TABLE IF EXISTS `tokens`;
CREATE TABLE IF NOT EXISTS `tokens` (
  `id_joueur` int NOT NULL,
  `token` TEXT NOT NULL,
  `time` int NOT NULL,
  KEY `token_ibfk_1` (`id_joueur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `aretes`
--
ALTER TABLE `aretes`
  ADD CONSTRAINT `aretes_ibfk_1` FOREIGN KEY (`id_case1`) REFERENCES `cases` (`id_case`),
  ADD CONSTRAINT `aretes_ibfk_2` FOREIGN KEY (`id_case2`) REFERENCES `cases` (`id_case`);

--
-- Contraintes pour la table `cases`
--
ALTER TABLE `cases`
  ADD CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`id_continent`) REFERENCES `continents` (`id_continent`),
  ADD CONSTRAINT `cases_ibfk_2` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

--
-- Contraintes pour la table `continents`
--
ALTER TABLE `continents`
  ADD CONSTRAINT `continents_ibfk_1` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

--
-- Contraintes pour la table `etat_partie`
--
ALTER TABLE `etat_partie`
  ADD CONSTRAINT `etat_partie_ibfk_1` FOREIGN KEY (`id_cases`) REFERENCES `cases` (`id_case`),
  ADD CONSTRAINT `etat_partie_ibfk_2` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`),
  ADD CONSTRAINT `etat_partie_ibfk_3` FOREIGN KEY (`id_partie`) REFERENCES `parties` (`id_partie`);

--
-- Contraintes pour la table `joueurs_parties`
--
ALTER TABLE `joueurs_parties`
  ADD CONSTRAINT `joueurs_parties_ibfk_1` FOREIGN KEY (`id_partie`) REFERENCES `parties` (`id_partie`),
  ADD CONSTRAINT `joueurs_parties_ibfk_2` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`),
  ADD CONSTRAINT `joueurs_parties_ibfk_3` FOREIGN KEY (`id_joueursuivant`) REFERENCES `joueurs` (`id_joueur`);

--
-- Contraintes pour la table `parties`
--
ALTER TABLE `parties`
  ADD CONSTRAINT `parties_ibfk_1` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);

--
-- Contraintes pour la table `tokens`
--
ALTER TABLE `tokens`
  ADD CONSTRAINT `token_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueurs` (`id_joueur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
