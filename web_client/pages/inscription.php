<?php
session_start();
if (isset($_SESSION["user"])) unset($_SESSION["user"]);
?>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Risk en ligne | Inscription</title>
    <link rel="stylesheet" href="../style/style.css">
    <link rel="icon" href="../content/images/RISK-32.png">
</head>
<body>
<header id="header">
    <div id="header__logo">
        <img src="../content/images/RISK-32.png" alt="logo">
        <h2>RISK</h2>
    </div>
</header>
<section id="register_form">
    <a href="../index.php">Retour</a>
    <?php if (isset($_SESSION["register_error"])) { ?>
        <p>
            <?php
            echo $_SESSION["register_error"];
            unset($_SESSION["register_error"]);
            ?>
        </p>
    <?php } ?>
    <form action="../index.php" method="post" id="register_form__form">
        <div id="register_form__form__username">
            <input type="text" name="register_username" placeholder="Choisissez un nom d'utilisateur">
        </div>
        <div id="register_form__form__password">
            <input type="password" name="register_password" placeholder="Choisissez un mot de passe">
        </div>
        <input type="submit" value="Inscription" id="register_form__form__submit_button">
    </form>
    <div id="register_form__login">
        <a href="./connexion.php">Déjà inscrit ? Connectez-vous ici.</a>
    </div>
</section>

</body>
</html>
