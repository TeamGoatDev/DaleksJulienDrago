levelNumber = 1

class Dalek:
	dalekCount = 0

	def _init_(self,posX, posY):
		self.posX = posX
		self.posY = posY
		Dalek.dalekCount += 1

class TasFerraille:
	tasFerraileCount = 0

	def _init_(self,posX, posY):
		self.posX = posX
		self.posY = posY
		TasFerraille.tasFerraileCount += 1


listDalek = []
listFerraille = []

for i in range(5*levelNumber):
	listDalek.append(Dalek(i))



def gestionColission(self):
	for i in listDalek:    	#Prend le premier de la liste
		for e in listDalek:		#Fais le tour de la liste avec les informations du premier
			if i != e:				#Vérifie si ce n'est pas les mêmes points dans la liste
				if i.posX == e.posX:	#Compare les deux positions en X des deux daleks
					if i.posY == e.posY:	#Compare les deux positions en Y des deux daleks
						listFerraille.append(TasFerraille(x))		#Si oui, on créer un objet tas de feraille pour l'introduire dans la liste
						listFerraille[tasFerraileCount].posX = i.posX		#Prend le position du premier dalek pour l'attribuer au tas de feraille
						listFerraille[tasFerraileCount].posY = i.posY		#Prend le position du premier dalek pour l'attribuer au tas de feraille




	
