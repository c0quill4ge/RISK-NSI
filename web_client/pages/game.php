<?php
session_start();
error_reporting(E_ALL);
ini_set("display_errors", 1);

if (!isset($_SESSION["user"])) {
    header("Location: inscription.php");
    exit();
} else {
    $playerId = $_SESSION["user"];
}
function random_str_generator($len_of_gen_str): string
{
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&#@*%$";
    $var_size = strlen($chars);
    $random_str = '';

    for ($x = 0; $x < $len_of_gen_str; $x++) {
        $random_str .= $chars[rand(0, $var_size - 1)];
    }

    return $random_str;
}

$createNewGame = isset($_GET["create_new_game"]) && $_GET["create_new_game"] == "true";

include_once "../PHP/database.php";
$database = new Database();
?>
<!doctype html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Risk en ligne | Jouer</title>
    <link rel="shortcut icon" href="../content/images/RISK-32.png" type="image/x-icon">
    <link rel="stylesheet" href="../style/style.css">
</head>
<body>
<main id="main_game">
<!--    <img src="../content/svg/Risk_board.svg" alt="board svg" id="main_game__board">-->
    <?php
    $file = file('../content/svg/Risk_board.svg'); //importe la table de risk à partir de la 3ème ligne
    for($i=2;$i<sizeof($file);$i++){
        echo $file[$i];
    }
    ?>
</main>




<?php
$token = random_str_generator(256);
$database->registerToken($token, $playerId);
$c = "<script>const token = '{$token}';</script>";
echo $c;
?>
<script src="../script/script.js"></script>
<script src="../script/main.js"></script>
</body>
</html>
