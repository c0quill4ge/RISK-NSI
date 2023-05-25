<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Risk en ligne</title>
    <link rel="shortcut icon" href="./content/images/RISK-32.png" type="image/x-icon">
    <link rel="stylesheet" href="style/game.css">
</head>
<body>

<header id="header">
    <div id="header__logo">
        <img src="./content/images/RISK-32.png" alt="logo">
        <h2>RISK</h2>
    </div>
    <div id="header__menu">
        <ul>
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Règles</a></li>
            <li><a href="#">Jouer</a></li>
            <li><a href="#">À propos</a></li>
            <li><a href="#">Se connecter</a></li>
        </ul>
    </div>
</header>

<main id="main">
    <div id="main__home">
        <div id="main__home__game">
            <img src="./content/svg/Risk_board.svg" alt="risk board">
        </div>
        <div id="main__home_description">
            <h2>Découvrez risk en ligne</h2>
            <p>C'est comme le jeu de société sauf que c'est en ligne ! Vous jouez même contre des vraies personnes !</p>
        </div>
    </div>

    <div id="main__rules">
        <!--règles...-->
    </div>

    <div id="main__play">
        <a id="main__play__create" href="./pages/game.php?create_new_game=true">
            Créer une partie
        </a>
        <div id="main__play__list">
            <?php
            include_once "./PHP/getGames.php";
            foreach ($gameList as $gameId) {
            ?>
                <a href="./pages/game.php?game_id=<?=$gameId?>" id="main_play_join"></a>
            <?php
            }
            ?>
        </div>

    </div>
</main>

</body>
</html>