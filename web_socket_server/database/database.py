import datetime

import mariadb

from web_socket_server.database import database_ids


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
        query = "SELECT id_joueur, token, time FROM tokens WHERE token = ?;"
        self.cursor.execute(query, (token,))
        result = self.cursor.fetchone()
        current_timestamp = int(datetime.datetime.now().timestamp())
        if result:
            query = "DELETE FROM tokens WHERE token = ?;"
            self.cursor.execute(query, (token,))
            if current_timestamp - result[2] < 20: # 20 secondes pour utiliser le token avant sa suppression
            #if current_timestamp - result[2] < 20000: # modification de test, à supprimer à la mise en prod
                return True, result[0]
        return False, None

    def updateArmy(self, idpartie, coord, nb_troupe):  # Met à jour le nombre de troupe sur une case
        idcase = self.getCase(idpartie, coord)[2]
        query = "UPDATE etat_partie SET nb_pions VALUES ? WHERE id_partie = ? AND id_case = ? ;"
        self.cursor.execute(query, (nb_troupe, idpartie, idcase))

    def getPartie(self, idpartie):  # renvoie toutes les infos concernant les cases de la partie
        query = "SELECT (*) FROM etat_partie WHERE id_partie = ? ;"
        self.cursor.execute(query, (idpartie,))
        return self.cursor.fetchall()  # Renvoie liste de tuples [(id_partie, id_case, id_joueur, nb_pions)], avec un tuple par case

    def getCase(self, idpartie, coord):  # coord est un tuple (x,y)
        query = "SELECT nb_pions, id_joueurs, id_case FROM etat_partie JOIN case ON etat_partie.id_case = case.id_case WHERE id_partie = ? AND x = ? AND y = ?"
        self.cursor.execute(query, (idpartie, coord[0], coord[1]))
        case = self.cursor.fetchall()  # Unr liste contenant un seul tuple
        case = case[0]  # Afin de récupérer le seul tuple de la liste
        return case  # Renvoie le tuple du nb de pions et l'id du joueur et celui de la case

    def recupere_bdd(self, table, nom_champ, conditions_dict=None):
        # conditions_dict se présente comme un dictionnaire dont les clés et les valeurs sont des tuples
        # dont la première valeur est le séparateur et la deuxième la valeur de la condition à respecter
        # exemple : conditions_dict = {"id_joueur":("=",1),"pseudo":("LIKE","%a%")}

        # renvoie les valeurs sous forme de tuple de la bdd en fonction de la table et nom de champ en paramètre

        if conditions_dict == None:
            query = "SELECT {} FROM {};".format(nom_champ, table)
            self.cursor.execute(query)
            return self.cursor.fetchall()

        if not isinstance(conditions_dict, dict):
            raise TypeError("conditions_dict doit être un dictionnaire")

        query = "SELECT {} FROM {} WHERE"
        conditions = [nom_champ, table]

        for key, value in conditions_dict.items():
            if not isinstance(key, str):
                raise TypeError("La clé du dictionnaire doit être une chaîne de caractères")
            if not isinstance(value, tuple):
                raise TypeError("La valeur du dictionnaire doit être un tuple")
            if len(value) != 2:
                raise ValueError("Le tuple doit contenir deux valeurs")
            if not isinstance(value[0], str):
                raise TypeError("La première valeur du tuple doit être une chaîne de caractères")
            if not isinstance(value[1], str) and not isinstance(value[1], int):
                raise TypeError("La deuxième valeur du tuple doit être une chaîne de caractères ou un entier")

            if len(conditions_dict) == 1:
                query = query % value[0]
                conditions.append(key)
                conditions.append(value[1])
            else:
                if len(conditions) == 2:
                    query += " {} %s {} " % value[0]
                else:
                    query += " AND {} %s {} " % value[0]
                conditions.append(key)
                conditions.append(value[1])

        query += ";"
        query = query.format(*conditions)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def enregistrer_bdd(self, D):  # d => dict, faudra ptet modifier après, y'a ptet des erreurs dans la récupération des données
        for table in D:
            self.cursor.execute("SELECT id FROM ? ;", (table,))
            nb_ids = list(self.cursor)
            self.connection.commit()

            while len(nb_ids[0]) < len(table['id']):
                self.cursor.execute("INSERT INTO ? ? VALUES ? ;",
                                    (table, table.keys(), (table[column][len(nb_ids[0])] for column in table),))
                self.connection.commit()

                self.cursor.execute("SELECT id FROM ? ;", (table,))
                nb_ids = list(self.cursor)
                self.connection.commit()

            for column in table:
                for id_entry in range(0, len(column.values())):
                    self.cursor.execute("UPDATE ? SET ? = ? WHERE id = ?;", (table, column, column[id_entry]),
                                        id_entry, )
                    self.connection.commit()

    def updateProperty(self, idpartie, idcase, id_new_owner):  # Lorsqu'un joueur prend un pays
        query = "UPDATE id_joueur FROM etat_partie VALUES ? WHERE id_case = ? AND id_partie = ?;"
        self.cursor.execute(query, (id_new_owner, idcase, idpartie))