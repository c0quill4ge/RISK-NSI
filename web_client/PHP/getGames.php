<?php
include_once "database.php";

$database = new Database();

$gameList = $database->getGames();