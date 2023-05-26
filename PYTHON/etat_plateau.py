
import random
from web_socket_server/database/database.py import Database

def attaquer(database, graphe, idpartie, id_joueur, id_case_dep, id_case_cib, nb_troupe):  # Possible que si le nb de troupe est strictement supérieur à 1
    nb_pions_case_dep, id_joueur = database.getCase(idpartie, id_case_dep)
    nb_pions_case_cib, id_joueur_ennemie = database.getCase(idpartie, id_case_cib)
    # On s'assure que le nb de troupes n'est pas abusé, que l'on attaque un autre joueur et que le chemin entre les 2 cases existent
    if nb_troupe <= nb_pions_case_dep and id_joueur != id_joueur_ennemie and graphe.verifier_voisins(id_case_dep, id_case_cib): 
    	pertes = bataille_des(nb_troupe, nb_pions_case_cib)
    	new_nb_troupe_att = nb_troupe - pertes[0]
    	new_nb_troupe_def = nb_troupe_def - pertes[1]
    	if new_nb_troupe_att < 1:  # L'attaquant ne peux pas avoir moins d'une troupe sur son pays
            new_nb_troupe_att = 1
    	if new_nb_troupe_def < 1:  # Le défenseur a perdu son pays
            database.updateProperty(idpartie, id_case_cib, id_joueur)
            database.updateArmy(idpartie, id_case_cib, 1)
    	else:
            database.updateArmy(idpartie, id_case_cib, new_nb_troupe_def)
    	database.updateArmy(idpartie, id_case_dep, new_nb_troupe_att)  # Met à jour l'armée de l'attaquant

def bataille_des(pions_att, pions_def):  # Renvoie le tuple des pertes de chaque côtés
    if pions_att >= 3:
        att = [random.randint(1, 6) for _ in range(3)]
    else:
        att = [random.randint(1, 6) for _ in range(pions_att)]
    if pions_def >= 2:
        déf = [random.randint(1, 6) for _ in range(2)]
    else:
        déf = [random.randint(1, 6)]

    att.sort(reverse=True)
    déf.sort(reverse=True)
    perte_att, perte_déf = 0, 0
    l = min(len(att), len(déf))
    for i in range(l):
        if att[i] > déf[i]:
            perte_déf += 1
        else:
            perte_att += 1
    return (perte_déf, perte_att)

def deplacer_troupes(id_partie, case_depart, case_arrivée, nb_troupes):
	
    db = Database()
    G = creer_graphe(id_partie) 
    Partie = db.getPartie(id_partie) # liste de tuples [(id_case, id_joueur, nb_pions)], avec un tuple par case

    def get_joueur(id_case0):
        for id_case, id_joueur, nb_pions in Partie:
            if id_case == id_case0:
                return id_joueur     
    def get_nb_pions(id_case0):
        for id_case, id_joueur, nb_pions in Partie:
            if id_case == id_case0:
                return id_joueur

    if get_joueur(case_depart) != tour(id_partie):
        raise NbPionsInsuffisant
    joueur = tour(id_partie)
    

    #check que ya assez de nm troupes dans case arrive
    if get_nb_pions(case_depart) <= nb_troupes:
        raise CaseNonValide

    #verifier chemin case depart case arrive (condition = meme territoire)
    test = False 
    visited = dict()
    f = File()
    f.enfiler(case_depart)
    while not (f.est_vide()):
        a = f.defiler()
        if a not in visited and get_joueur(a) == joueur: # on verifie que la case nest pas visite ET elle appartient au joueur dont cest le tour 
            visited[a]= True
            if a == case_depart:
                test = True
            for v in G.voisins(a):
                f.enfiler(v)

    if not test:# case impossible a connecter
        raise CasesNonConnectes

    #update le nombre dans les deux cases, deplacement de nb_troupes de case_depart à case_arrivée
    
    db.updateArmy(id_partie, case_depart, get_nb_pions(case_depart)-nb_troupes)
    db.updateArmy(id_partie, case_arrivée, get_nb_pions(case_arrivée)+nb_troupes)

    return

def changer_tour(id_partie):
	#une fois que le joueur a joué, on passe au joueur suivant
    pass

def tour(D,id_partie): # D => bdd
	#renvoie le numéro du joueur qui doit jouer
    return partie["tour"] if partie["id_partie"] == id_partie for partie in D["partie"]


def donner_troupes(D,id_partie, joueur): # D => base de donnée sous forme de dictionnaire
	nb_territoires = 0
	for partie in D["etat_partie"]:
	    if partie["id_partie"] == id_partie and joueur == partie["id_joueur"]:
		nb_territoires = len(partie["id_cases"])

		nb_troupes_a_ajouter = nb_territoires // 3  # on donne autant d'armées que le joueur a de territoires divisé par 3 (sans le reste lol)
		partie["nb_pions"] += nb_troupes_a_ajouter
		break
	enregistre_bdd(D)
	

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
