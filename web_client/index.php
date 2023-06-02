<?php
session_start();
require_once "./PHP/database.php";
$database = new Database();

if (isset($_POST["register_username"]) && isset($_POST["register_password"])) {
    $create = $database->createUser($_POST["register_username"], $_POST["register_password"]);
    if (is_string($create)) {
        $_SESSION["register_error"] = $create;
        header("Location: /pages/inscription.php");
        exit;
    }
    $_SESSION["user"] = intval($create);
    header("Location: index.php");
    exit;

}

if (isset($_POST["login_username"]) && isset($_POST["login_password"])) {
    $log = $database->login($_POST["login_username"], $_POST["login_password"]);
    if (is_string($log)) {
        $_SESSION["login_error"] = $log;
        header("Location: /pages/connexion.php");
        exit;
    }
    $_SESSION["user"] = intval($log);
    header("Location: index.php");
    exit;
}

$login = $_SESSION["user"] ?? null;
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Risk en ligne</title>
    <link rel="shortcut icon" href="./content/images/RISK-32.png" type="image/x-icon">
    <link rel="stylesheet" href="style/style.css">
</head>
<body>

<header id="header">
    <div id="header__logo">
        <img src="./content/images/RISK-32.png" alt="logo">
        <h2>RISK</h2>
    </div>
    <div id="header__menu">
        <ul>
            <li><a href="#main__home">Accueil</a></li>
            <li><a href="#main__rules">Règles</a></li>
            <li><a href="#main__play">Jouer</a></li>
            <li><a href="#main__about">À propos</a></li>
            <?php if ($login == null) { ?>
                <li><a href="#main__login">Se connecter</a></li>
            <?php } ?>
            <li><a href="./pages/connexion.php">Se déconnecter</a></li>
        </ul>
    </div>
</header>

<main id="main">
    <div id="main__home">
        <div id="main__home__game">
            <img src="./content/svg/Risk_board.svg" alt="risk board">
        </div>
        <div id="main__home_description">
            <h1>Découvrez risk en ligne</h1>
            <p>C'est comme le jeu de société sauf que c'est en ligne ! Vous jouez même contre des vraies personnes !</p>
        </div>
    </div>

    <div id="main__rules">
        <h1>RISK-NSI</h1>
        <p>Règles du jeu</p>

        <p>Phase de placement:</p>
        <ul>
            <li>les objectifs sont distribués aux joueurs (facultatif si on fixe un objectif plus simple comme conquérir 60% du plateau ...)</li>
            <li>les terrains sont attribués aléatoirement aux joueurs, avec un pion sur chaque case</li>
            <li>les joueurs disposent alors chacun son tour, un par un, les pions restants</li>
        </ul>

        <p>Phase de jeu</p>
        <ul>
            <li>Dans un tour:</li>
            <ul>
                <li>les joueurs reçoivent leurs pions et les placent</li>
                <li>les joueurs peuvent effectuer une ou plusieurs attaques</li>
                <li>les joueurs peuvent effectuer des déplacements</li>
            </ul>
            <li>Un joueur qui atteint son objectif a gagné.</li>
        </ul>

        <p>Déroulement d'une attaque</p>
        <ul>
            <li>si un joueur le souhaite, il sélectionne une de ses cases, un certain nombre des pions de sa case, et une case voisine qu'il ne contrôle pas</li>
            <li>un clic sur "attaquer" va lancer une bataille de dés. Selon les résultats, des pions attaquants ou défenseurs vont mourir</li>
            <li>s'il ne reste plus de pion défenseur, les pions sélectionnés vont occuper la case, qui est alors conquise</li>
        </ul>

        <p>Déplacements</p>
        <ul>
            <li>À la fin du tour, un joueur peut sélectionner des pions d'une case et les envoyer vers une autre case, à condition qu'il existe un chemin les reliant en passant par ses cases</li>
        </ul>

    </div>

    <div id="main__play">
        <a id="main__play__create" href="./pages/game.php?create_new_game=true">
            Créer une partie
        </a>
        <div id="main__play__list">
            <?php
            include_once "./PHP/getGames.php";
            global $gameList;
            if (count($gameList) == 0) { ?>
                <p>Aucune partie n'est en cours, créez-en une !</p>
            <?php } else {
                foreach ($gameList as $gameInfos) { ?>
                    <div id="main__play__list__game">
                        <h2><?= $gameInfos["nom_plateau"] ?></h2>
                        <p><?= $gameInfos["nb_joueurs"] ?> joueurs</p>
                        <a href="./pages/game.php?game_id=<?= $gameInfos["id_partie"] ?>" id="main_play_join">rejoindre
                            la partie</a>
                    </div>
                <?php }
            }?>
        </div>
    </div>

    <div id="main__about">
        <h1>À propos</h1>
        <p>Projet réalisé par la classe de NSI de Terminale du Lycée Henri Poincaré à Nancy en tant que projet de fin d'année.</p>
    </div>

    <?php if ($login == null) { ?>
        <div id="main__login">
            <h1>Se connecter</h1>
            <a href="./pages/connexion.php">Se connecter</a>
        </div>
    <?php } ?>


</main>

</body>
</html>