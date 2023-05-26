<?php
session_start();
$playerId = $_SESSION["login"];
$createNewGame = $_GET["create_new_game"]=="true";
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
</head>
<body>
<?php
function random_str_generator($len_of_gen_str) {
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&#@*%$";
    $var_size = strlen($chars);
    $random_str = '';

    for ($x = 0; $x < $len_of_gen_str; $x++) {
        $random_str .= $chars[rand(0, $var_size - 1)];
    }

    return $random_str;
}

$token = random_str_generator(256);

include_once "../PHP/database.php";
$database = new Database();

$database->registerToken($token, $playerId);

$c = "<script>const token = '{$token}';</script>";

echo $c;
?>
<script src="../script/script.js"></script>
</body>
</html>
