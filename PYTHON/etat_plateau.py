from class_graphe import *
import random
from web_socket_server.database.database import Database

class NbPionsInsuffisant(Exception):
    "lorsque le nombreeeee de pions qu'on depalce ou avec lequel on attaque est trop grand"
    pass
class CasesNonConnectes(Exception):
    "lorsque on ne peut pas passer d'une case a l'autre sans passer sur le terriotire d'autrui ou alors ces cases ne sont pas voisines"
    pass
class CaseNonValide(Exception):
    "lorsque la case n'appartient pas au joueur dont cest le tour"
    pass

#####################################################################"
# voir dans attaquer et donner troupes dans plateau.py pour le bonus de continent
###########
 
class LogiqueDuJeu:
	def __init__(self):
		self.db = Database()
		self.id_partie = db.getLastGame()
		
		
	def attaquer(self,database, id_attaquant, id_case_dep, id_case_cib,nb_troupe, nb_troupes_envoyées):  # Possible que si le nb de troupe est strictement supérieur à 1
		idpartie = self.id_partie
		graphe = database.graphe
		nb_pions_case_dep, id_joueur = database.getCase(idpartie, id_case_dep)
		nb_pions_case_cib, id_joueur_ennemie = database.getCase(idpartie, id_case_cib)
	    # On s'assure que le nb de troupes n'est pas abusé, que l'on attaque un autre joueur et que le chemin entre les 2 cases existent
		if nb_troupe <= nb_pions_case_dep and id_joueur != id_joueur_ennemie and graphe.verifier_voisins(id_case_dep,id_case_cib):
			pertes = bataille_des(nb_troupe, nb_pions_case_cib)
			new_nb_troupe_att = nb_troupe - pertes[0]
			new_nb_troupe_def = nb_troupe_def - pertes[1]
			if new_nb_troupe_att < 1:  # L'attaquant ne peux pas avoir moins d'une troupe sur son pays
				new_nb_troupe_att = 1
			if new_nb_troupe_def < 1:  # Le défenseur a perdu son pays
				database.updateProperty(idpartie, id_case_cib, id_joueur)
				change_couleur(idpartie, id_case_cib, id_attaquant)
				deplacer_troupes(idpartie,id_case_dep,id_case_cib,nb_troupes_envoyées)
				# verifier si le joueur possede un continent en entier: envoyer le message qu'il a obtenu tout un continent donc qu'il possede un bonus

				database.updateArmy(idpartie, id_case_cib, 1)
			else:
				database.updateArmy(idpartie, id_case_cib, new_nb_troupe_def)
			database.updateArmy(idpartie, id_case_dep, new_nb_troupe_att)  # Met à jour l'armée de l'attaquant
		elif nb_troupe > nb_pions_case_dep:
			raise NbPionsInsuffisant
		elif id_joueur == id_joueur_ennemie:
			raise CaseNonValide
		elif not graphe.verifier_voisins(id_case_dep, id_case_cib):
			raise CasesNonConnectes

	def bataille_des(self,pions_att, pions_def):  # Renvoie le tuple des pertes de chaque côtés
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



	def deplacer_troupes(self, case_depart, case_arrivée, nb_troupes):
		id_partie = self.id_partie
		Partie = self.db.getPartie(id_partie) # liste de tuples [(id_case, id_joueur, nb_pions)], avec un tuple par case
		graphe = database.graphe
		def get_joueur(id_case0):
			for id_case, id_joueur, nb_pions in Partie:
				if id_case == id_case0:
					return id_joueur     
		def get_nb_pions(id_case0):
			for id_case, id_joueur, nb_pions in Partie:
				if id_case == id_case0:
					return id_joueur
		
		if get_joueur(case_depart) != tour(id_partie):
			raise CaseNonValide
		joueur = tour(id_partie)


	    #check que ya assez de nm troupes dans case arrive
		if get_nb_pions(case_depart) <= nb_troupes:
			raise NbPionsInsuffisant

	    #verifier chemin case depart case arrive (condition = meme territoire)
	    #parcours en largeur du graphe
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
					for v in graphe.voisins(a):
						f.enfiler(v)
		
		if not test:# case impossible a connecter
			raise CasesNonConnectes

	    #update le nombre dans les deux cases, deplacement de nb_troupes de case_depart à case_arrivée
		self.db.updateArmy(id_partie, case_depart, get_nb_pions(case_depart)-nb_troupes)
		self.db.updateArmy(id_partie, case_arrivée, get_nb_pions(case_arrivée)+nb_troupes)
		return

	def changer_tour(self):
		id_partie = self.id_partie
		#une fois que le joueur a joué, on passe au joueur suivant
		joueursuivant = self.db.recupere_bdd("joueurs_partie","tour",{"id_partie":("=",id_partie)})
		#mettre a la place de joueur
		joueurs = self.db.recupere_bdd("joueurs_partie","id_joueur",{"id_partie":("=",id_partie)}) #order by id_joueur limit 1
		for joueur in range(len(joueurs)-1):
			if joueurs[joueur] == joueursuivant:
				if joueur == len(joueurs)-1:
					joueurdapres = joueurs[0]
				else:
					joueurdapres = joueurs[joueur+1]
		self.db.enregistrer_bdd("joueurs_parties","joueur_suivant",joueurdapres,{"id_partie":id_partie})
		self.db.enregistrer_bdd("parties","tour",joueursuivant,{"id_partie",id_partie})


	def tour(self):
		#renvoie le numéro du joueur qui doit jouer
		return self.db.recupere_bdd("partie","tour",{"id_partie":("=",self.id_partie)})


	def donner_troupes(self, joueur):

		# si bonus de continent -> donner plus de troupes
		nb_territoires = 0
		nb_territoires = len(self.db.recupere_bdd("etat_partie","id_cases",{"id_partie":("=",self.id_partie),"id_joueur":("=",id_joueur)}))

		nb_troupes_a_ajouter = nb_territoires // 3  # on donne autant d'armées que le joueur a de territoires divisé par 3 (sans le reste lol)
		partie["nb_pions"] += nb_troupes_a_ajouter



	def debut_partie(self,id_partie):
	    # donne n troupes à tous les joueurs
	    # donne les territoires aléatoirement à tous les joueurs
	    # fonction placement_troupes
		id_partie = self.id_partie
		territoires = list(self.db.recuperer_bdd('cases', 'id_cases', {'id_partie' : ("=",id_partie)}))
		shuffle(territoires)
		n = len(territoires) / 6
		terres = [territoires[i:i + n] for i in range(0, len(territoires), n)]
		L = list(self.db.recuperer_bdd("joueurs", "id_joueur", {'id_partie': ("=",id_partie)}))
		i = 0
		for id_player in L:
			db.donner_troupes(id_player)
			self.db.insert_bdd("etat_partie",{"id_partie":id_partie,"id_cases":terres[i],"id_joueur":id_player,"nb_pion":1})
			i += 1
		assert i == 6, "probleme boucle debut partie"


	def placement_troupes(self,database, id_case, nb_troupes = 1):
		#vérifie si c’est en début de partie → le joueur ne peut poser qu’une troupe
		state = self.db.recupere_bdd("parties","etat",{"id_partie":("=",self.id_partie)})
		if state == "debut":
			#on donne une troupe à id_case d'id_partie
			self.db.updateArmy(self.id_partie, id_case, 1)
		else:
			#sinon place nb_troupes troupes sur la case voulue	
			self.db.updateArmy(self.id_partie, id_case, nb_troupes)


	def change_couleur(self, id_case, id_nouveau_joueur):
	    return {'order':change_couleur,'id_case':id_case, 'id_joueur':id_nouveau_joueur}
	
	def return_plateau(self):
		dico = dict()
		cases = self.db.getPartie(idpartie) # # Renvoie liste de tuples [(id_case, id_joueur, nb_pions)], avec un tuple par case
		for case in cases :
			if not case[0] in dico:
				dico[case[0]] = (case[1],case[2])

		return dico
	
	def deroulement(D=dict()):
		id_partie = None
		if D == dict():
			db.insert_bdd("parties",{"id_plateau":1 ,"etat":"debut"})
			id_partie = db.getLastGame()
			debut_partie(id_partie)
		else:
			for keys in D.keys():
				if key in self.__web_server.get_functions.keys():
					self.__web_server.execute_function(*D[key])
					
			
		
		return return_plateau(id_partie)
	
	def check_bonus_continent(id_partie): # renvoie une liste de tuple des joueurs avec le continent qu'ils possèdent
	      joueurs_bonus = []
	      id_plateau = recupere_bdd("parties","id_plateau",{"id_partie":("=",id_partie)})
	      continents = recupere_bdd("continents","id_continent",{"id_plateau":("=",id_plateau)})
	      for continent in continents:
		    cases_continent = recupere_bdd("cases","id_case",{"id_plateau":("=",id_plateau),"id_continent" : ("=",continent)})
		    joueur1 = recupere_bdd("etat_partie","id_joueur",{"id_case":("=",cases_continent[0])})
		    for i in range(1,len(cases_continent)-1):
			  joueur = recupere_bdd("etat_partie","id_joueur",{"id_case":("=",cases_continent[i])})
			  if joueur != joueur1:
				break
		    joueurs_bonus.append((continent,joueur1))
	      return joueurs_bonus

