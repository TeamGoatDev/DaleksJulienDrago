import Modele
import Vue

class Controller:
	def _init_(self):
		self.visuel = Vue(self)
		self.modele = MainBoard(self)
	
	def CommencerJeu(self):
		self.visuel.afficherMenu()

