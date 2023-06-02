<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css" />
    <title>Document</title>
</head>
<body>

    <?php
    session_start();
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
    include('..\PHP\sql_methodes.php');
    if (! ISSET($_SESSION["id"])){ 
        header("Location: inscription.php");
        exit();
    } else {
        $id =$_SESSION["id"];
    }
    
    $bdd=sql_connect();
    $requete = 'SELECT pseudo FROM joueurs WHERE id_joueur=:id;';
    $req = $bdd->prepare($requete);
    $req->bindParam(":id",$id);
    $req->execute();
    $tableau = $req->fetchAll(PDO::FETCH_ASSOC);
    echo'<div class ="nom">votre pseudo: '.htmlspecialchars( $tableau[0]['pseudo'])."</div>";
    
    $requete = 'SELECT parties.id_partie,parties.tour,parties.etat FROM parties join joueurs_parties on partie.id_parties = joueurs_parties.id_parties WHERE joueurs_parties.id_joueur=:id;';
    $req = $bdd->prepare($requete);
    $req->bindParam(":id",$id);
    $req->execute();
    $tableau = $req->fetchAll(PDO::FETCH_ASSOC);
    
    echo'<div class ="nom">votre nombre de parties jouées: '.count($tableau)."</div>";
    
    
    ?>
    <div class='puissance'>
    <table class="tableau_style">
        <tr>
            <td class='case'>id_partie</td>
            <td class='case'>tour</td>
            <td class='case'>etat</td>
          

        </tr>
        <?php
        foreach($tableau as $k =>$v){
            echo'<tr>';
            foreach($v as $k1=>$v1){
                echo'<td class="case">'.$v1.'</td>';
            }
            echo'</tr>';
        }
        ?>
    </table>
    </div>
</body>
</html>
