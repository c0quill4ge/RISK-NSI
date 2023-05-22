import mariadb
import random
conn = mariadb.connect(
    user="root",
    password="",
    host= "localhost",
    port=3307,
    database="risk"
)


def attaquer(id_partie, case_depart, case_arrivée, nb_troupes):
	#fonction lancer_de et l’analyse et trouve le vainqueur
	#recommence jusqu’à épuisement d’une des troupes et renvoie le vainqueur de l’attaque
    pass

def lancer_de(id_partie, joueur):
	#renvoie le resultat du lancer de 2 dés en random de 1 à 6 (vainqueur / vaincu)
    pass

def deplacer_troupes(id_partie, case_depart, case_arrivée, nb_troupes):
	#deplacer nb_troupes de case_depart à case_arrivée
    pass

def changer_tour(id_partie):
	#une fois que le joueur a joué, on passe au joueur suivant
    pass

def tour(id_partie):
	#renvoie le numéro du joueur qui doit jouer
    pass

def donner_troupes(id_partie, joueur):
	#en fonction du nombre de pays possédés, le jeu donne n troupes au joueur pendant la partie
    pass

def debut_partie(id_partie):
	#donne n troupes à tous les joueurs
	#donne les territoires aléatoirement à tous les joueurs
	#fonction placement_troupes
    pass

def placement_troupes(id_partie, id_case, nb_troupes = 1):
	#vérifie si c’est en début de partie → le joueur ne peut poser qu’une troupe
	#sinon place nb_troupes troupes sur la case voulue
    pass

def enregistre_bdd(D):
    # D est un dictionnaire de dictionnaires
    # D = {nomdelatable (de la bdd) : {nomduchamp : valeurdenomduchamp}
    pass

def recupere_bdd(id_partie):
    # renvoyer un dictionnaire de dictionnaires R
    # R = {nomdelatable : {nomduchamp : valeurdenomduchamp}
    curseur = conn.cursor()
    curseur.execute("SELECT id_joueur_suivant FROM joueurs_partie WHERE id_partie = ? ;", (idpartie,))
    joueur_suivant = curseur