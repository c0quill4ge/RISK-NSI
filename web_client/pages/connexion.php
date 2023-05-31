<?php
session_start();
if (isset($_SESSION["user"])) unset($_SESSION["user"]);
?>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Risk en ligne | Connexion</title>
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
<section id="connect_form">
    <a href="../index.php">Retour</a>
    <?php if (isset($_SESSION["login_error"])) { ?>
        <p>
            <?php
            echo $_SESSION["login_error"];
            unset($_SESSION["login_error"]);
            ?>
        </p>
    <?php } ?>
    <form action="../index.php" method="post" id="connect_form__form">
        <div id="connect_form__form__username">
            <input type="text" name="login_username" placeholder="Votre nom d'utilisateur">
        </div>
        <div id="connect_form__form__password">
            <input type="password" name="login_password" placeholder="Votre mot de passe">
        </div>
        <input type="submit" value="Connexion" id="connect_form__form__submit_button">
    </form>
    <div id="connect_form__register">
        <a href="./inscription.php">Vous n'avez pas de compte ?</a>
    </div>
</section>

</body>
</html>