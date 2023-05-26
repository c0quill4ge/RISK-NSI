<?php
include('server.php');
$username = null;


// INSCRIPTION UTILISATEUR

?>

<!DOCTYPE html>
<html>
<head>
    <title>Inscription Risk</title>
    <link rel="stylesheet" type="text/css" href="../style/style.css">
</head>
<body>
<div class="header">
    <section>

    </section>
</div>

<form method="post" class="content" action="../PHP/analyse.php?sens=inscription.php">

    <div class="input-group">
        <label>Pseudonyme:</label>
        <input type="text" name="pseudo">
    </div>
    <div>
        <label>Age:</label>
        <input type="int" name="age" ">
    </div>
    <div>
        <label>MDP:</label>
        <input type="password" name="mdp">
    </div>
    <div>
        <button type="submit">S'inscrire</button>
    </div>
    <p>
        Vous possédez déjà un compte ? <a href="connexion.php">Connexion</a>
    </p>
</form>
</body>
</html>