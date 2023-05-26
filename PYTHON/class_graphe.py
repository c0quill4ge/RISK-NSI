class Graphe:
    def __init__(self):
        self.__adj = dict() # dictionnaire de dictionnaire

    def sommet_existe(self,s):
        return s in self.__adj

    def ajouter_arc(self,s1,s2,poids=1):
        s1,s2 = str(s1),str(s2)

        assert self.sommet_existe(s1), "Le sommet " + s1 + " n'existe pas"
        assert self.sommet_existe(s2), "Le sommet " + s2 + " n'existe pas"
        assert not self.verifier_voisins(s1, s2), "Un arc existe déjà entre les sommets " + s1 + " et " + s2
        assert type(poids) == int or type(poids) == float, "Le poids doit être un entier ou un réel"

        self.__adj[s1][s2] = poids

    def supprimer_arc(self,s1,s2):
        s1,s2 = str(s1),str(s2)

        assert self.sommet_existe(s1), "Le sommet " + s1 + " n'existe pas"
        assert self.sommet_existe(s2), "Le sommet " + s2 + " n'existe pas"
        assert self.verifier_voisins(s1, s2), s1 + " et " + s2 + " ne sont pas voisins"

        del self.__adj[s1][s2]

    def ajouter_sommet(self,s):
        s = str(s)

        assert not self.sommet_existe(s), "Le sommet " + s + " existe déjà"

        self.__adj[s] = dict()

    def supprimer_sommet(self,s):
        s = str(s)

        assert self.sommet_existe(s), "Le sommet " + s + " n'existe pas"

        del self.__adj[s]
        for s1 in self.__adj:
            if s in self.__adj[s1]:
                del self.__adj[s1][s]

    def ajouter_arete(self,s1,s2,poids=1):
        s1,s2 = str(s1),str(s2)

        assert self.sommet_existe(s1), "Le sommet " + s1 + " n'existe pas"
        assert self.sommet_existe(s2), "Le sommet " + s2 + " n'existe pas"
        assert not self.verifier_voisins(s1, s2), "Un arc existe déjà entre les sommets " + s1 + " et " + s2
        assert not self.verifier_voisins(s2, s1), "Un arc existe déjà entre les sommets " + s2 + " et " + s1
        assert type(poids) == int or type(poids) == float, "Le poids doit être un entier ou un réel"

        self.ajouter_arc(s1,s2,poids)
        self.ajouter_arc(s2,s1,poids)

    def supprimer_arete(self,s1,s2):
        s1,s2 = str(s1),str(s2)

        assert self.sommet_existe(s1), "Le sommet " + s1 + " n'existe pas"
        assert self.sommet_existe(s2), "Le sommet " + s2 + " n'existe pas"
        assert self.verifier_voisins(s1, s2), "Il n'y a pas d'arc entre les sommets " + s1 + " et " + s2
        assert self.verifier_voisins(s2, s1), "Il n'y a pas d'arc entre les sommets " + s2 + " et " + s1

        self.supprimer_arc(s1,s2)
        self.supprimer_arc(s2,s1)

    def voisins(self,s):
        s = str(s)

        assert self.sommet_existe(s), "Le sommet " + s + " n'existe pas"

        return list(self.__adj[s].keys())

    def verifier_voisins(self,s1,s2):
        s1,s2 = str(s1),str(s2)

        assert self.sommet_existe(s1), "Le sommet " + s1 + " n'existe pas"
        assert self.sommet_existe(s2), "Le sommet " + s2 + " n'existe pas"

        voisins = self.voisins(s1)
        for v in voisins:
            if v == s2:
                return True
        return False

    def liste_sommets(self):
        return list(self.__adj.keys())

    def __repr__(self):
        rep = ""
        for s1 in self.__adj:
            rep += s1 + ":" + ",".join(self.voisins(s1)) + "\n"
        return rep

    def __contains__(self, e):
        # Si e est un tuple (a, b) : vérifie que l'arc a -> b existe
        # Si e est une chaîne de caractères : vérifie que le sommet e existe

        assert type(e) == tuple or type(e) == str

        if type(e) == tuple:
            assert len(e) == 2
            return self.verifier_voisins(e[0], e[1])
        elif type(e) == str:
            return self.sommet_existe(e)

    def verifier_chemin(self, chemin):
        # Retourne True si chemin est un chemin du graphe et False sinon
        for i in range(len(chemin) - 1):
            if not self.sommet_existe(chemin[i]) or not self.sommet_existe(chemin[i+1]) or not self.verifier_voisins(chemin[i],chemin[i+1]):
                return False
        return True
        
    def poids_chemin(self, chemin):
        # retourne le poids total du chemin dans le graphe
        # ou fait une erreur si le chemin n'existe pas

        assert self.verifier_chemin(chemin)
        
        p = 0
        for i in range(len(chemin) - 1):
            p += self.__adj[chemin[i]][chemin[i+1]]
        return p