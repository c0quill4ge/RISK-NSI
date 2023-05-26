<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
session_start();
$sens=$_GET['sens'];
include("sql_methodes.php");
$bdd = sql_connect();
if ($sens=="inscription"){ 
    $Name = $_POST["pseudo"];
    $mdp = $_POST["mdp"];
    //On enregistre le nom, mdp dans clients
    $requete = 'INSERT INTO joueurs VALUES (:n, MD5(:c));';
    $req = $bdd->prepare($requete);
    $req->bindParam(":c",$mdp);
    $req->bindParam(":n",$Name);
    $req->execute();
    if ($req->rowCount() == 0){
        header("Location: inscription.php?problem=nom_deja_pris");
        exit();
    }
    
    $_SESSION["id"] = $bdd->lastInsertId();

    header("Location: index.php");
    exit();

}elseif ($sens=="connexion"){
    $Name = $_POST["pseudo"];
    $mdp = $_POST["mdp"];
    //connexion
    $requete = 'SELECT id FROM joueurs WHERE pseudo = :n AND mdp = MD5(:c);';
    $req = $bdd->prepare($requete);
    $req->bindParam(":c",$mdp);
    $req->bindParam(":n",$Name);
    $req->execute();
    $tableau = $req->fetchAll(PDO::FETCH_ASSOC);
    // le tableau contient l'id si le pseudo et le mdp conviennent, sinon ya rien


 
    if (ISSET($tableau[0]["id"])){
        $_SESSION["id"] = $tableau[0]["id"];

        
        header("Location: index.php");
        exit(); 
    } else {
        header("Location: connexion.php?problem=login_info");
        exit();
    }
}
?>