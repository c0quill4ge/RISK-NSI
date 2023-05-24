<!DOCTYPE html>
<?php session_start();?>
<html>
	<head>
		<link rel = "stylesheet" src = "style_main.css">
	</head>
	<script type = "text/javascript" src = "main.js"></script>
	<?php
		$file = file('Risk_board.svg'); //importe la table de risk à partir de la 3ème ligne
		for($i=2;$i<sizeof($file);$i++){
			echo $file[$i];
		}
	?>
</html>