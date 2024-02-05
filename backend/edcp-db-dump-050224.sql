-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le : lun. 05 fév. 2024 à 11:20
-- Version du serveur : 5.7.39
-- Version de PHP : 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `edcp-db`
--

-- --------------------------------------------------------

--
-- Structure de la table `casexemptions`
--

CREATE TABLE `casexemptions` (
  `id` int(11) NOT NULL,
  `casexemption` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `categoriedcps`
--

CREATE TABLE `categoriedcps` (
  `id` int(11) NOT NULL,
  `categoriedcp` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `categorietraits`
--

CREATE TABLE `categorietraits` (
  `id` int(11) NOT NULL,
  `categorie` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `categorietraits`
--

INSERT INTO `categorietraits` (`id`, `categorie`) VALUES
(1, ' catégorie D'),
(2, ' catégorie A');

-- --------------------------------------------------------

--
-- Structure de la table `correspondants`
--

CREATE TABLE `correspondants` (
  `id` int(11) NOT NULL,
  `organisation_id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenoms` varchar(100) NOT NULL,
  `fonction` varchar(100) NOT NULL,
  `lettreacceptation` varchar(100) NOT NULL,
  `lettredecision` varchar(100) NOT NULL,
  `created` date NOT NULL,
  `cv` varchar(100) NOT NULL,
  `cj` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `demdeautorisations`
--

CREATE TABLE `demdeautorisations` (
  `id` int(11) NOT NULL,
  `created` date NOT NULL,
  `organisation_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `finalite_id` int(11) NOT NULL,
  `descfinalite` varchar(100) NOT NULL,
  `fondjuridique_id` int(11) NOT NULL,
  `persconcernee_id` int(11) NOT NULL,
  `casexemption_id` int(11) NOT NULL,
  `categoriedcp_id` int(11) NOT NULL,
  `statut` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `enregistrements`
--

CREATE TABLE `enregistrements` (
  `id` int(11) NOT NULL,
  `created` int(11) NOT NULL,
  `organisation_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finalites`
--

CREATE TABLE `finalites` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `sensible` varchar(100) NOT NULL,
  `ordre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `finalites`
--

INSERT INTO `finalites` (`id`, `label`, `sensible`, `ordre`) VALUES
(1, 'Gestion de la paie', '0', 0),
(2, 'Gestion des Ressources Humaines ', '0', 0);

-- --------------------------------------------------------

--
-- Structure de la table `fonctions`
--

CREATE TABLE `fonctions` (
  `id` int(11) NOT NULL,
  `fonction` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `fondjuridiques`
--

CREATE TABLE `fondjuridiques` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `fondjuridiques`
--

INSERT INTO `fondjuridiques` (`id`, `label`, `description`) VALUES
(1, 'Consentement des personnes concernées', 'Le consentement est recueilli au moment de la collecte des données'),
(2, 'Exécution d\'un contrat', 'Le traitement est effectué....'),
(3, 'Obligation légale', 'Les données sont traitées...'),
(4, 'Mission d\'intérêt public', 'Les données sont traitées...'),
(5, 'Sauvegarde des intérêts vitaux', 'Le traitement vise à...');

-- --------------------------------------------------------

--
-- Structure de la table `habilitations`
--

CREATE TABLE `habilitations` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `fonction_id` int(11) NOT NULL,
  `created` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `journallogs`
--

CREATE TABLE `journallogs` (
  `id` int(11) NOT NULL,
  `created` date NOT NULL,
  `action` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `journaltransactions`
--

CREATE TABLE `journaltransactions` (
  `id` int(11) NOT NULL,
  `created` date NOT NULL,
  `transaction` varchar(100) NOT NULL,
  `cible` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `listeenregistrements`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `listeenregistrements` (
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `listeentreprises`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `listeentreprises` (
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `listesousfinalites`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `listesousfinalites` (
`id` int(11)
,`label` varchar(100)
,`sensible` tinyint(1)
,`ordre` int(11)
,`finalite` varchar(100)
,`finalite_id` int(11)
);

-- --------------------------------------------------------

--
-- Structure de la table `organisations`
--

CREATE TABLE `organisations` (
  `id` int(11) NOT NULL,
  `typeclient_id` int(11) NOT NULL,
  `raisonsocial` varchar(100) NOT NULL,
  `presentation` tinytext NOT NULL,
  `rccm` varchar(100) NOT NULL,
  `secteur_id` int(11) NOT NULL,
  `tel` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `ville_id` int(11) NOT NULL,
  `adresse_geo` varchar(100) NOT NULL,
  `website` varchar(100) NOT NULL,
  `coordonneesgps` varchar(100) NOT NULL,
  `categorietrait_id` int(11) NOT NULL,
  `effectifs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `organisations`
--

INSERT INTO `organisations` (`id`, `typeclient_id`, `raisonsocial`, `presentation`, `rccm`, `secteur_id`, `tel`, `email`, `ville_id`, `adresse_geo`, `website`, `coordonneesgps`, `categorietrait_id`, `effectifs`) VALUES
(1, 1, 'Bergnaum Inc', 'intangible', '618848405', 3, '(634) 901-5582', 'guest@mail.com', 1, 'Abidjan – Marcory Anoumabo\r\n', 'https://www.autoritedeprotection.ci/', '5.312063625661596, -3.9650586631134037', 1, 78),
(2, 2, 'Dickinson, Raynor and Rosenbaum', 'leading edge', '168192562', 4, '216.417.5831 x18307', 'Randall_Hintz60@gmail.com', 2, 'Treichville, Km4 Bd de Marseille', 'https://esatic.ci/presentation/', '72R2+7F Abidjan', 2, 80);

-- --------------------------------------------------------

--
-- Structure de la table `pays`
--

CREATE TABLE `pays` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `pays`
--

INSERT INTO `pays` (`id`, `label`) VALUES
(1, 'Norfolk Island'),
(2, 'Saint Helena'),
(3, 'Côte d\'Ivoire');

-- --------------------------------------------------------

--
-- Structure de la table `persconcernees`
--

CREATE TABLE `persconcernees` (
  `id` int(11) NOT NULL,
  `label` varchar(100) DEFAULT NULL,
  `sensible` tinyint(1) NOT NULL,
  `ordre` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `persconcernees`
--

INSERT INTO `persconcernees` (`id`, `label`, `sensible`, `ordre`) VALUES
(1, 'Salariés', 0, 0),
(2, 'Clients', 0, 0),
(3, 'Visiteurs', 0, 0),
(4, 'Etudiants', 0, 0),
(5, 'Elèves', 0, 0),
(6, 'Enfants', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `registrations`
--

CREATE TABLE `registrations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `typeclient_id` int(11) NOT NULL,
  `raisonsociale` varchar(100) NOT NULL,
  `representant` varchar(100) NOT NULL,
  `rccm` varchar(100) DEFAULT NULL,
  `secteur_id` int(11) DEFAULT NULL,
  `secteur_description` varchar(100) DEFAULT NULL,
  `presentation` varchar(255) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `email_contact` varchar(100) DEFAULT NULL,
  `site_web` varchar(100) DEFAULT NULL,
  `pays_id` varchar(100) DEFAULT NULL,
  `ville` varchar(100) DEFAULT NULL,
  `adresse_geo` varchar(100) DEFAULT NULL,
  `adresse_bp` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `roles`
--

INSERT INTO `roles` (`id`, `role`) VALUES
(1, 'Usager'),
(2, 'Opérateur'),
(99, 'Administrateur');

-- --------------------------------------------------------

--
-- Structure de la table `secteurs`
--

CREATE TABLE `secteurs` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `sensible` tinyint(1) NOT NULL,
  `ordre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `secteurs`
--

INSERT INTO `secteurs` (`id`, `label`, `sensible`, `ordre`) VALUES
(1, 'Agro-industrie', 0, 0),
(2, 'Santé', 0, 0),
(3, 'Banque', 0, 0),
(4, 'Télécommunications', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `sousfinalites`
--

CREATE TABLE `sousfinalites` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `sensible` tinyint(1) NOT NULL,
  `ordre` int(11) NOT NULL,
  `finalite_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `sousfinalites`
--

INSERT INTO `sousfinalites` (`id`, `label`, `sensible`, `ordre`, `finalite_id`) VALUES
(1, 'Déclaration des salariés auprès de la CNPS/CGRAE', 0, 0, 2),
(2, 'Respect des obligations en matière sociales', 0, 0, 2),
(3, 'Création de compte client', 1, 0, 1),
(4, 'Edition de carte bancaire pour les client', 0, 0, 1);

-- --------------------------------------------------------

--
-- Structure de la table `typeclients`
--

CREATE TABLE `typeclients` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `sensible` tinyint(11) DEFAULT NULL,
  `ordre` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `typeclients`
--

INSERT INTO `typeclients` (`id`, `label`, `description`, `sensible`, `ordre`) VALUES
(1, 'Personne physique', 'Personne agissant pour son propre compte', 0, 0),
(2, 'Entreprise privée', 'Entreprises individuelle, PME, grandes entreprises etc.', 0, 0),
(3, 'Administrations publiques', 'Ministères, institutions, sociétés d\'Etat etc.', 0, 0),
(4, 'ONG / Association', 'Organisations à but non lucratifs, associations, groupements etc.', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(100) NOT NULL,
  `passwd` varchar(100) NOT NULL,
  `role_id` int(11) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `createdAt` datetime DEFAULT NULL,
  `nom` varchar(100) NOT NULL,
  `prenoms` varchar(100) DEFAULT NULL,
  `organisation` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telephone` varchar(100) NOT NULL,
  `fonction` varchar(100) NOT NULL,
  `consentement` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `login`, `passwd`, `role_id`, `avatar`, `createdAt`, `nom`, `prenoms`, `organisation`, `email`, `telephone`, `fonction`, `consentement`) VALUES
(41, 'john_doe', 'sha256$7SD2su4Bu9OB4Cn8$17890477290fe85b735d9ecca0ee14e630a2734cb7a57ee52c99ad713aceee5e', 1, 'https://example.com/avatar.jpg', '2023-11-17 00:00:00', 'Doe', 'John', 'Example Organization', 'john.doe@example.com', '1234567890', 'Developer', '1'),
(42, 'Fourier', 'sha256$eMdnkZ3tPa66c5yx$cee011e26ad35fc8eb6809b67e0149af2d3e4f5da63a679c0e488bbd5cce2576', 1, 'https://example.com/avatar.jpg', '2023-11-17 00:00:00', 'Doe', 'John', 'Example Organization', 'john.doe@example.com', '1234567890', 'Developer', '1'),
(43, 'Fourier', 'sha256$TRC3qbKszmXeOA6d$6b81c63f30ceedf7f8815fa87ef4ee016e93efcd9b0bfe185f05a23046a08973', 1, 'https://example.com/avatar.jpg', '2023-11-17 00:00:00', 'Doe', 'John', 'Example Organization', 'john.doe@example.com', '1234567890', 'Developer', '1'),
(44, 'Yapi', 'sha256$BZoe3bMlWvGUIepL$59d48efe5d8fec52eb9e4ffe55af0a71db2bfd3580473570400e09ad0cbc34bf', 1, 'https://example.com/avatar.jpg', '2023-11-27 00:00:00', 'yapa', 'yapo', 'Example Organization', 'yapa.yapo@example.com', '1234567890', 'Jurisste', '1'),
(46, 'Kouassi', 'sha256$Bb5PLk8DLFQw8yLk$469df155eb456afaef99194c74a420318fff643302cb5d02126ee20ad03f493a', 1, 'https://example.com/avatar.jpg', '2023-11-28 12:28:32', 'kouassi', 'kouassi', 'Example Organization', 'kouassi.yapo@example.com', '0240636123', 'Comptable', '1'),
(47, 'guest', 'sha256$v01djYVhfqWAxwSP$655423bea3d389fc834d6426582433d3b780c226adca97bfbde1b12c31452340', 1, 'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/253.jpg', NULL, 'Lafayette', 'Hagenes', 'Funk LLC', 'guest1@mail.com', '(768) 222-1783', 'Dynamic Usability Developer', '1'),
(48, 'guest', 'sha256$2QCGb2innSysJquN$2cf5e113f45fc63046137df000b1ca47b19995d4336c005630bb0be4c678fe2c', 1, 'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/253.jpg', NULL, 'Lafayette', 'Hagenes', 'Funk LLC', 'guest2@mail.com', '(768) 222-1783', 'Dynamic Usability Developer', '1'),
(56, 'guest', 'sha256$JHYch6nD9rP4eR5F$f6b90b2412b2c574328203335ea057921b9c806c1a9991f0c508cb566fa146d8', 1, '', NULL, 'GUEST', 'Guest', 'G Corp', 'guest@mail.com', '01 02 03 04 05', 'Directeur Général', '1'),
(57, 'manager', 'sha256$ffDw6ngZqhWTkkJu$fd05ae9f2f72f24d94a3c91a05de551aa5444cad59689327090fed17676012b8', 2, '', NULL, 'MANA', 'Manager', 'ARTCI', 'manager@mail.com', '01 02 03 04 05', 'Gestionnaire', '1'),
(58, '', 'sha256$PQfodbeLHgioALjt$c2d5c4783e12e9798d23c90e895ea8949ea9483d052032667478a977f0a7096c', 1, '', NULL, '', '', '', 'guest2@mail.com', '', '', '0'),
(59, '', 'sha256$XijGS1834zGQ1IHg$c2562c8d40cbb709e5039a0132842ff56b9bf8b001dd046daa86e811d962d973', 1, '', NULL, '', '', '', 'guest3@mail.com', '', '', '0');

-- --------------------------------------------------------

--
-- Structure de la table `villes`
--

CREATE TABLE `villes` (
  `id` int(11) NOT NULL,
  `label` varchar(100) NOT NULL,
  `pays_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `villes`
--

INSERT INTO `villes` (`id`, `label`, `pays_id`) VALUES
(1, 'Jamestown', 2),
(2, 'Raymond', 1);

-- --------------------------------------------------------

--
-- Structure de la vue `listeenregistrements`
--
DROP TABLE IF EXISTS `listeenregistrements`;

CREATE ALGORITHM=UNDEFINED DEFINER=`Uroot_edcp`@`localhost` SQL SECURITY DEFINER VIEW `listeenregistrements`  AS SELECT `a`.`id` AS `id`, `a`.`created` AS `created`, `b`.`typeclient` AS `typeclient`, `b`.`nomRaisonsocial` AS `nomRaisonsocial`, `b`.`presentation` AS `presentation`, `b`.`numRccm` AS `numRccm`, `b`.`domaine` AS `domaine`, `b`.`telephone` AS `telephone`, `b`.`contactEmail` AS `contactEmail`, `b`.`pays` AS `pays`, `b`.`ville` AS `ville`, `b`.`localisation` AS `localisation`, `b`.`gmapslink` AS `gmapslink`, `b`.`cateDonnees` AS `cateDonnees`, `b`.`effectifs` AS `effectifs`, `a`.`user_id` AS `user_id` FROM (`enregistrements` `a` join `listeentreprises` `b`) WHERE (`a`.`organisation_id` = `b`.`id`)  ;

-- --------------------------------------------------------

--
-- Structure de la vue `listeentreprises`
--
DROP TABLE IF EXISTS `listeentreprises`;

CREATE ALGORITHM=UNDEFINED DEFINER=`Uroot_edcp`@`localhost` SQL SECURITY DEFINER VIEW `listeentreprises`  AS SELECT `a`.`id` AS `id`, `b`.`typeclient` AS `typeclient`, `a`.`raisonsocial` AS `nomRaisonsocial`, `a`.`presentation` AS `presentation`, `a`.`rccm` AS `numRccm`, `c`.`label` AS `domaine`, `a`.`tel` AS `telephone`, `a`.`email` AS `contactEmail`, `f`.`pays` AS `pays`, `d`.`ville` AS `ville`, `a`.`adresse_geo` AS `localisation`, `a`.`website` AS `website`, `a`.`coordonneesgps` AS `gmapslink`, `e`.`categorie` AS `cateDonnees`, `a`.`effectifs` AS `effectifs` FROM (((((`organisations` `a` join `typeclients` `b`) join `secteurs` `c`) join `villes` `d`) join `categorietraits` `e`) join `pays` `f`) WHERE ((`a`.`typeclient_id` = `b`.`id`) AND (`c`.`id` = `a`.`secteur_id`) AND (`d`.`id` = `a`.`ville_id`) AND (`e`.`id` = `a`.`categorietrait_id`) AND (`f`.`id` = `d`.`pays_id`))  ;

-- --------------------------------------------------------

--
-- Structure de la vue `listesousfinalites`
--
DROP TABLE IF EXISTS `listesousfinalites`;

CREATE ALGORITHM=UNDEFINED DEFINER=`Uroot_edcp`@`localhost` SQL SECURITY DEFINER VIEW `listesousfinalites`  AS SELECT `a`.`id` AS `id`, `a`.`label` AS `label`, `a`.`sensible` AS `sensible`, `a`.`ordre` AS `ordre`, `b`.`label` AS `finalite`, `a`.`finalite_id` AS `finalite_id` FROM (`sousfinalites` `a` join `finalites` `b`) WHERE (`b`.`id` = `a`.`finalite_id`) ORDER BY `a`.`finalite_id` ASC  ;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `casexemptions`
--
ALTER TABLE `casexemptions`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `categoriedcps`
--
ALTER TABLE `categoriedcps`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `categorietraits`
--
ALTER TABLE `categorietraits`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `correspondants`
--
ALTER TABLE `correspondants`
  ADD PRIMARY KEY (`id`),
  ADD KEY `organisation_id` (`organisation_id`);

--
-- Index pour la table `demdeautorisations`
--
ALTER TABLE `demdeautorisations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `organisation_id` (`organisation_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `finalite_id` (`finalite_id`),
  ADD KEY `fondjuridique_id` (`fondjuridique_id`),
  ADD KEY `persconcernee_id` (`persconcernee_id`),
  ADD KEY `casexemption_id` (`casexemption_id`),
  ADD KEY `categoriedcp_id` (`categoriedcp_id`);

--
-- Index pour la table `enregistrements`
--
ALTER TABLE `enregistrements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `organisation_id` (`organisation_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Index pour la table `finalites`
--
ALTER TABLE `finalites`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `fonctions`
--
ALTER TABLE `fonctions`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `fondjuridiques`
--
ALTER TABLE `fondjuridiques`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `journallogs`
--
ALTER TABLE `journallogs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Index pour la table `journaltransactions`
--
ALTER TABLE `journaltransactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Index pour la table `organisations`
--
ALTER TABLE `organisations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `secteur_id` (`secteur_id`),
  ADD KEY `ville_id` (`ville_id`),
  ADD KEY `categorietrait_id` (`categorietrait_id`),
  ADD KEY `typeclient_id` (`typeclient_id`);

--
-- Index pour la table `pays`
--
ALTER TABLE `pays`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `persconcernees`
--
ALTER TABLE `persconcernees`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `registrations`
--
ALTER TABLE `registrations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Index pour la table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `secteurs`
--
ALTER TABLE `secteurs`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sousfinalites`
--
ALTER TABLE `sousfinalites`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finalite_id` (`finalite_id`);

--
-- Index pour la table `typeclients`
--
ALTER TABLE `typeclients`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- Index pour la table `villes`
--
ALTER TABLE `villes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pays_id` (`pays_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `casexemptions`
--
ALTER TABLE `casexemptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `categoriedcps`
--
ALTER TABLE `categoriedcps`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `categorietraits`
--
ALTER TABLE `categorietraits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `correspondants`
--
ALTER TABLE `correspondants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `demdeautorisations`
--
ALTER TABLE `demdeautorisations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `enregistrements`
--
ALTER TABLE `enregistrements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `finalites`
--
ALTER TABLE `finalites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `fonctions`
--
ALTER TABLE `fonctions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `fondjuridiques`
--
ALTER TABLE `fondjuridiques`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `journallogs`
--
ALTER TABLE `journallogs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `journaltransactions`
--
ALTER TABLE `journaltransactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `organisations`
--
ALTER TABLE `organisations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `pays`
--
ALTER TABLE `pays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `persconcernees`
--
ALTER TABLE `persconcernees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `registrations`
--
ALTER TABLE `registrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT pour la table `secteurs`
--
ALTER TABLE `secteurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `sousfinalites`
--
ALTER TABLE `sousfinalites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `typeclients`
--
ALTER TABLE `typeclients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT pour la table `villes`
--
ALTER TABLE `villes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `correspondants`
--
ALTER TABLE `correspondants`
  ADD CONSTRAINT `Correspondants_ibfk_1` FOREIGN KEY (`organisation_id`) REFERENCES `organisations` (`id`);

--
-- Contraintes pour la table `demdeautorisations`
--
ALTER TABLE `demdeautorisations`
  ADD CONSTRAINT `Demdeautorisations_ibfk_1` FOREIGN KEY (`organisation_id`) REFERENCES `organisations` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_3` FOREIGN KEY (`finalite_id`) REFERENCES `finalites` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_4` FOREIGN KEY (`fondjuridique_id`) REFERENCES `fondjuridiques` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_5` FOREIGN KEY (`persconcernee_id`) REFERENCES `persconcernees` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_6` FOREIGN KEY (`casexemption_id`) REFERENCES `casexemptions` (`id`),
  ADD CONSTRAINT `Demdeautorisations_ibfk_7` FOREIGN KEY (`categoriedcp_id`) REFERENCES `categoriedcps` (`id`);

--
-- Contraintes pour la table `enregistrements`
--
ALTER TABLE `enregistrements`
  ADD CONSTRAINT `Enregistrements_ibfk_1` FOREIGN KEY (`organisation_id`) REFERENCES `organisations` (`id`),
  ADD CONSTRAINT `Enregistrements_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `journallogs`
--
ALTER TABLE `journallogs`
  ADD CONSTRAINT `Journallogs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `journaltransactions`
--
ALTER TABLE `journaltransactions`
  ADD CONSTRAINT `Journaltransactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `organisations`
--
ALTER TABLE `organisations`
  ADD CONSTRAINT `Organisations_ibfk_1` FOREIGN KEY (`secteur_id`) REFERENCES `secteurs` (`id`),
  ADD CONSTRAINT `Organisations_ibfk_2` FOREIGN KEY (`ville_id`) REFERENCES `villes` (`id`),
  ADD CONSTRAINT `Organisations_ibfk_3` FOREIGN KEY (`categorietrait_id`) REFERENCES `categorietraits` (`id`),
  ADD CONSTRAINT `Organisations_ibfk_4` FOREIGN KEY (`typeclient_id`) REFERENCES `typeclients` (`id`);

--
-- Contraintes pour la table `registrations`
--
ALTER TABLE `registrations`
  ADD CONSTRAINT `fk_users_table` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `sousfinalites`
--
ALTER TABLE `sousfinalites`
  ADD CONSTRAINT `Sousfinalites_ibfk_1` FOREIGN KEY (`finalite_id`) REFERENCES `finalites` (`id`);

--
-- Contraintes pour la table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `Users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

--
-- Contraintes pour la table `villes`
--
ALTER TABLE `villes`
  ADD CONSTRAINT `Villes_ibfk_1` FOREIGN KEY (`pays_id`) REFERENCES `pays` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
