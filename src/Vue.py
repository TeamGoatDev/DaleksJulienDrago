from enum import Enum

class ActionJeu(enum):
	Haut = 1
	Bas = 2
	Gauche = 3
	Droite = 4

	Zap = 5
	Teleport = 6
	Rien = 7

	HautGauche = 8
	HautDroite = 9
	BasGauche = 10
	BasDroite = 11

class ActionMenu(enum):
	NouvellePartie = 1
	MeilleurScore = 2
	Quitter = 3

class Vue:
	def __init__(self,Controleur):
		self.controleur = Controleur

	def clearScreen(self):
		for i in range(100):
			print()	

	def afficherMenu(self):
		self.clearScreen()
		print()
		print("Jeu de Daleks")
		print("-------------")
		print("MENU: n (nouvelle partie)  -  m (meilleur score)  -  q (quitter)")
		touche=input("Votre choix: ")
		self.controleur.commandeVersself.tradcutionToucheMenu


	def affichageAireJeu(self, Modele):
		for i in range(.largeur):
			for w in range(.longueur):
				print("-")

	def tradcutionToucheMenu(self, touche):
		if touche == "n":
			return ActionMenu.NouvellePartie
		elif touche == "m":
			return ActionMenu.MeilleurScore
		elif touche == "q":
			return ActionMenu.Quitter		

	def traductionToucheJeu(self, touche):
		if touche == "w":
			return ActionJeu.Haut
		elif touche == "x":
			return ActionJeu.Bas
		elif touche == "a":
			return ActionJeu.Gauche
		elif touche == "d":
			return ActionJeu.Droite
		elif touche == "k":
			return ActionJeu.Zap
		elif touche == "s":
			return ActionJeu.Teleport
		elif touche == "n":
			return ActionJeu.Rien
		elif touche == "q":
			return ActionJeu.HautGauche
		elif touche == "e":
			return ActionJeu.HautDroite
		elif touche == "z":
			return ActionJeu.BasGauche
		elif touche == "c":
			return ActionJeu.BasDroite					

			
