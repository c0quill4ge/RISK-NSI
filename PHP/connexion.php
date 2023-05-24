<?php 
include('server.php');
$username = null;


// INSCRIPTION UTILISATEUR

?>

<!DOCTYPE html>
<html>
<head>
  <title>Connexion Risk</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div class="header">
<section>

</section>
  </div>

  <form method="post" class="content" action="analyse.php?sens=connexion">

  	<div>
  	  <label>Pseudonyme:</label>
  	  <input type="text" name="pseudo">
  	</div>
  	<div >
  	  <label>MDP:</label>
  	  <input type="password" name="mdp">
  	</div>
  	<div>
  	  <button type="submit">Se connecter</button>
  	</div>
  	<p>
  		Vous ne possédez pas de compte ? <a href="incription.php">Connexion</a>
  	</p>
  </form>
</body>
</html>
