<?php 
include('server.php');
$username = null;


// INSCRIPTION UTILISATEUR

?>

<!DOCTYPE html>
<html>
<head>
  <title>Inscription Risk</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div class="header">
<section>

</section>
  </div>

  <form method="post" class="content" action="analyse.php">

  	<div class="input-group">
  	  <label>Pseudonyme:</label>
  	  <input type="text" name="username" value="<?php echo $username; ?>">
  	</div>
	<div >
  	  <label>Age:</label>
  	  <input type="int" name="age" value="<?php echo $age; ?>">
  	</div>
  	<div >
  	  <label>MDP:</label>
  	  <input type="password" name="password_1">
  	</div>
  	<div >
  	  <label>Confirmer MDP:</label>
  	  <input type="password" name="password_2">
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