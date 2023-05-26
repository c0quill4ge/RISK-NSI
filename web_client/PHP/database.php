<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);

require_once "database_info.php";
class Database {
    private function sql_connect() {
        global $host;
        global $port;
        global $username;
        global $password;
        global $database;

        try {
            $sch = "mysql:host=" . $host . ";dbname=" . $database . ";port=" . $port;
            $bdd = new PDO($sch, $username, $password);
        } catch (Exception $e) {
            die("Erreur : " . $e->getMessage());
        }
        return $bdd;
    }

    public function getFromDatabaseCustomRequest($table, $nom_champ, $conditions_dict = null): array {
        if ($conditions_dict === null) {
            $query = "SELECT $nom_champ FROM $table;";
            $stmt = $this->sql_connect()->query($query);
            return $stmt->fetchAll();
        }

        if (!is_array($conditions_dict)) {
            throw new TypeError("conditions_dict doit être un dictionnaire");
        }

        $query = "SELECT %s FROM %s WHERE %s %s %s";
        $conditions = array($nom_champ, $table);

        foreach ($conditions_dict as $key => $value) {
            if (!is_string($key)) {
                throw new TypeError("La clé du tableau doit être une chaîne de caractères");
            }
            if (!is_array($value) || count($value) !== 2) {
                throw new ValueError("La valeur du tableau doit être un tableau contenant exactement deux valeurs");
            }
            if (!is_string($value[0])) {
                throw new TypeError("La première valeur du tableau doit être une chaîne de caractères");
            }
            if (!is_string($value[1]) && !is_int($value[1])) {
                throw new TypeError("La deuxième valeur du tableau doit être une chaîne de caractères ou un entier");
            }

            $separator = $value[0];
            $conditionValue = $value[1];

            if (count($conditions_dict) === 1) {
                array_push($conditions, $key, $separator, $conditionValue);
            } else {
                if (count($conditions) !== 2) {
                    $query .= "AND %s %s %s";
                }
                array_push($conditions, $key, $separator, $conditionValue);
            }

        }

        $query .= sprintf($query, ...$conditions) . ";";

        $stmt = $this->sql_connect()->prepare($query);
        $stmt->execute($conditions);
        return $stmt->fetchAll();
    }

    public function registerToken($token, $id) {
        $query = "INSERT INTO tokens (id_joueur, token, time) VALUES (:id, :token, UNIX_TIMESTAMP());";
        $stmt = $this->sql_connect()->prepare($query);
        $stmt->bindValue(':id', $id);
        $stmt->bindValue(':token', $token);

        try {
            $stmt->execute();
            return true;
        } catch (Exception $e) {
            return false;
        }
    }


}

$database = new Database();
$temp = $database->getFromDatabaseCustomRequest("joueurs", "*", array("pseudo" => array("=", "TESTACCOUNT")));
var_dump($temp);