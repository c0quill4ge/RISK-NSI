-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3307
-- Généré le : mer. 24 mai 2023 à 07:03
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
  `nb_pions` int(11) DEFAULT 0,
  PRIMARY KEY (`id_case`),
  KEY `id_continent` (`id_continent`),
  KEY `id_plateau` (`id_plateau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `cases`
--
ALTER TABLE `cases`
  ADD CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`id_continent`) REFERENCES `continents` (`id_continent`),
  ADD CONSTRAINT `cases_ibfk_2` FOREIGN KEY (`id_plateau`) REFERENCES `plateaux` (`id_plateau`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
