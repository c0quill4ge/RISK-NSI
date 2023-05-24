import datetime

import mariadb

class Database:
    def __init__(self):
        self.connection = mariadb.connect(
            user=database_ids.user,
            password=database_ids.password,
            host=database_ids.host,
            port=database_ids.port,
            database=database_ids.database
        )
        self.cursor = self.connection.cursor()

    def find_token(self, token: str):
        query = "SELECT id_joueur, token, time FROM tokens WHERE token = ?"
        self.cursor.execute(query, (token,))
        result = self.cursor.fetchone()
        current_timestamp = datetime.datetime.now().timestamp()
        if result:
            if current_timestamp - result[2] < 20:
                return True, result[0]
            else:
                query = "DELETE FROM tokens WHERE token = ?"
                self.cursor.execute(query, (token,))
        return False, None
    
    def updateArmy(self, idpartie, coord, nb_troupe):  # Met à jour le nombre de troupe sur une case
        idcase = getCase(idpartie, coord)[2]
        query = "UPDATE etat partie SET nb_pions VALUES ? WHERE id_partie = ? AND id_case = ? ;"
        self.cursor.execute(query, (nb_troupe, idpartie, idcase))

    def getPartie(self, idpartie):  # renvoie toutes les infos concernant les cases de la partie
        query = "SELECT (*) FROM etat partie WHERE id_partie = ? ;"
        self.cursor.execute(query, (idpartie,))
        return self.cursor.fetchall()  # Renvoie liste de tuples [(id_partie, id_case, id_joueur, nb_pions)], avec un tuple par case

    def getCase(self, idpartie, coord):  # coord est un tuple (x,y)
        query = "SELECT nb_pions, id_joueurs, id_case FROM etat partie JOIN case ON etat_partie.id_case = case.id_case WHERE id_partie = ? AND x = ? AND y = ?"
        self.cursor.execute(query, (idpartie, coord[0], coord[1]))
        case = self.cursor.fetchall()  # Unr liste contenant un seul tuple
        case = case[0]  # Afin de récupérer le seul tuple de la liste
        return case  # Renvoie le tuple du nb de pions et l'id du joueur et celui de la case
