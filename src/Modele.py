from random import randrange



class Dalek:
	def __init__(self,number,posX, posY):
		self.number = number
		self.posX = posX
		self.posY = posY

	def avancerVersDocteur(self, Docteur):
		if self.posX != Docteur.posX && self.posY != Docteur.posY:
			if self.posX > Docteur.posX && self.posY > Docteur.posY: #UpLeft
				self.posX -= 1
				self.posY -= 1
			elif self.posX > Docteur.posX && self.posY < Docteur.posY: #DownLeft
				self.posX -= 1
				self.posY += 1
			elif self.posX < Docteur.posX && self.posY > Docteur.posY: #UpRight
				self.posX += 1
				self.posY -= 1
			elif self.posX < Docteur.posX && self.posY < Docteur.posY: #DownRight
				self.posX += 1
				self.posY += 1
		elif self.posX == Docteur.posX && self.posY != Docteur.posY:
			if self.posY < Docteur.posY:
				self.posY += 1
			elif self.posY > Docteur.posY:
				self.posY -= 1
		elif self.posX != Docteur.posX && self.posY == Docteur.posY:
			if self.posX < Docteur.posX:
				self.posX += 1
			elif self.posX > Docteur.posX:
				self.posX -= 1			


class Docteur:

	def __init__(self, posX, posY):
		self.posX = posX
		self.posY = posY
		self.creditsCosmiques = 0
		self.nombreZap = 1

	def zapper(self,listDalek):
		if self.nombreZap >= 1:
			self.nombreZap -= 1
			for i in listDalek:
				if i.posX - self.posX == 1 || i.posX - self.posX == -1 || i.posX - self.posX == 0:  
					if i.posY - self.posY == 1 || i.posY - self.posY == 1 || i.posY - self.posY == 1:
						listDalek.pop(listDalek.index(i))


	def teleporter(self):
		teleportationPossible = false

		while teleportationPossible == false:
			pass






	def action(self, mouvement)
		if mouvement =		
							



class TasFerraille:

	tasFerrailleCount = 0

	def __init__(self,number,posX, posY):
		self.number = number
		self.posX = posX
		self.posY = posY
		TasFerraille.tasFerrailleCount += 1


class MainBoard:
	def __init__(self,controleur):
		self.levelNumber = 1
		self.largeur = 20
		self.longueur = 30
		self.listDalek = []
		self.listFerraille = []
		self.doc = Docteur()

	def gestionCollision(self):
		for i in listDalek:    	#Prend le premier de la liste
			for e in listDalek:		#Fais le tour de la liste avec les informations du premier
				if i != e:				#Vérifie si ce n'est pas les mêmes points dans la liste
					if i.posX == e.posX:	#Compare les deux positions en X des deux daleks
						if i.posY == e.posY:	#Compare les deux positions en Y des deux daleks
							self.listFerraille.append(TasFerraille(x, i.posX, i.posY))		#Si oui, on créer un objet tas de feraille pour l'introduire dans la liste
							self.listDalek.pop(listDalek.index(i))
							self.listDalek.pop(listDalek.index(e))

		for i in listDalek:    	#Commence une boucle dans la liste de dalek
			for q in listFerraille:		#Commence une boucle imbriqué dans la liste des tas de ferrailles
				if i.posX == q.posX:	#Vérifie si un des positions en X de dalek interferent avec un tas de ferraille
					if i.posY == q.posY:	#Vérifie la même chose en position Y
						self.listDalek.pop(listDalek.index(i))	#Si il ya une concordance parfaite dans les positions, on élimine le dalek courant


	def commencerNiveau(self, levelNumber):
		for i in range(5*levelNumber):
			self.listDalek.append(Dalek(i, random.randint(0,19) , random.randint(0,29) ))
		PosDepartDocOK = false
		NbDalekPasSurMemeCaseDoc = 0
		while PosDepartDocOK == false:			#Boucle qui génère une position aléatoire pour le doc
			self.doc.posX = random.randint(0,19)
			self.doc.posY = random.randint(0,29)
			for i in listDalek:					#Boucle testant la position de chaque nouveau dalek
				if i.posX != self.doc.posX:			
					if i.posY != self.doc.posY:
						NbDalekPasSurMemeCaseDoc += 1 		#Compte le nombre de dalek qui ne sont pas sur la même case que le docteur
			if NbDalekPasSurMemeCaseDoc == 5*levelNumber:
				PosDepartDocOK = true

	