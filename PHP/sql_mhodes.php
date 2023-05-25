<?php 
/* définition de fonctions en lien avec SQL, appelées depuis les autres parties du programme */
function sql_connect() {
    // fonction permettant de se connecter à la BDD
    // Les lignes suivantes sont à modifier selon les besoins !
    $dbname = 'risk';
    $identifiant = 'root'; //cet utilisateur n'a qu'un seul droit : lecture sur base BLOC4
    $motdepasse = '';
    $port = 3307;   
    try
    { 
        $sch='mysql:host=localhost;dbname='.$dbname.';port='.$port;
        $bdd = new PDO($sch , $identifiant, $motdepasse);
    }
    catch(Exception $e)
    {
        die('Erreur : '.$e->getMessage());
    }
    return $bdd ;
} /* se connecte à la bdd et renvoie l'objet PDO obtenu */


?>
