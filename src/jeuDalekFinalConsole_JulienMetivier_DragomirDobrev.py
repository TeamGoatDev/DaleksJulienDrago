import random
import sys
################################################################################
#                Modele *Class Docteur, Dalek et Ferraille*                    #
################################################################################
class ActionJeu():
    Haut = 1
    Bas = 2
    Gauche = 3
    Droite = 4
    Zap = 5
    Teleportation = 6
    Rien = 7
    HautGauche = 8
    HautDroite = 9
    BasGauche = 10
    BasDroite = 11
    Quitter = 12

class ActionMenu():
    NouvellePartie = 1
    MeilleurScore = 2
    Quitter = 3


class Dalek:
    def __init__(self,posX, posY):
        self.posX = posX
        self.posY = posY

    def avancerVersDocteur(self, Docteur):
        if self.posX != Docteur.posX and self.posY != Docteur.posY:
            if self.posX > Docteur.posX and self.posY > Docteur.posY: #UpLeft
                self.posX-=1
                self.posY-=1
            elif self.posX > Docteur.posX and self.posY < Docteur.posY: #DownLeft
                self.posX-=1
                self.posY+=1
            elif self.posX < Docteur.posX and self.posY > Docteur.posY: #UpRight
                self.posX+=1
                self.posY-=1
            elif self.posX < Docteur.posX and self.posY < Docteur.posY: #DownRight
                self.posX+=1
                self.posY+=1
        elif self.posX == Docteur.posX and self.posY != Docteur.posY:
            if self.posY > Docteur.posY: #Up
                self.posY-=1
            elif self.posY < Docteur.posY: #Down
                self.posY+=1
        elif self.posX != Docteur.posX and self.posY == Docteur.posY:
            if self.posX > Docteur.posX: #Left
                self.posX-=1
            elif self.posX < Docteur.posX: #Right
                self.posX+=1

class TasFerraille:

    def __init__(self,posX, posY):
        self.posX = posX
        self.posY = posY

class Docteur:
    def __init__(self,largeur,hauteur):
        self.posX = None
        self.posY = None
        self.largeur = largeur
        self.hauteur = hauteur
        self.creditsCosmiques = 0
        self.nombreZap = 0

    #À l'appel de cette fonction, nous devons passer dans les paramètres, la liste des daleks selon le modele, soit Partie.listDalek[]
    def zapper(self,listDalek):
        if self.nombreZap > 0:
            self.nombreZap -= 1
            for dalek in listDalek:
                if dalek.posX - self.posX == 1 or dalek.posX - self.posX == -1 or dalek.posX - self.posX == 0:  
                    if dalek.posY - self.posY == 1 or dalek.posY - self.posY == -1 or dalek.posY - self.posY == 0:
                        listDalek.pop(listDalek.index(dalek))
                        self.creditsCosmiques += 5

    def teleporter(self,listDalek,listFerraille):
        self.teleportationPossible = False

        while self.teleportationPossible == False:
            countOfDalek = 0
            randomX = random.randrange(self.largeur)
            randomY = random.randrange(self.hauteur)

            for ferraille in listFerraille:
                if ferraille.posX == randomX and ferraille.posY == randomY:
                    break
            else:
                for dalek in listDalek:
                    if dalek.posX == randomX and dalek.posY == randomY:
                            break
                else:
                    for dalek in listDalek:
                        if dalek.posX - randomX == 1 or dalek.posX - randomX == -1 or dalek.posX - randomX == 0:  
                            if dalek.posY - randomY == 1 or dalek.posY - randomY == -1 or dalek.posY - randomY == 0:
                                break
                        countOfDalek += 1

            if countOfDalek == len(listDalek):
                self.teleportationPossible = True
            
        self.posX = randomX
        self.posY = randomY

###############################################################################
#                                    Partie                                   #
###############################################################################     
        
class Partie:
    def __init__(self,largeur,hauteur):
        self.niveau = 0
        self.daleksParNiveau = 5
        self.largeur=largeur
        self.hauteur=hauteur
        self.niveauFini = False
        self.partieFini = False
        self.docteur=Docteur(self.largeur, self.hauteur)
        self.listDalek = []
        self.listFerraille = []
        self.creeNiveau()



    def creeNiveau(self):
        self.niveau += 1
        self.docteur.nombreZap += 1
        xx = random.randrange(self.largeur)
        yy = random.randrange(self.hauteur)
        self.docteur.posX = xx
        self.docteur.posY = yy
        self.listFerraille = []
        nombreDeDalek = self.niveau*self.daleksParNiveau
        tempPosDocteur = [[self.docteur.posX, self.docteur.posY]]
        while len(self.listDalek) < nombreDeDalek:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            if [x,y] not in tempPosDocteur:
                if self.listDalek:
                    for dal in self.listDalek:
                        if x != dal.posX and y != dal.posY:
                            self.listDalek.append(Dalek(x,y))
                            break
                else:
                    self.listDalek.append(Dalek(x,y))
 
 
 
    def gestionCollision(self):
        for i in self.listDalek:     #Prend le premier de la liste
            for e in self.listDalek:     #Fais le tour de la liste avec les informations du premier
                if i != e:              #Vérifie si ce n'est pas les mêmes points(daleks) dans la liste
                    if i.posX == e.posX:    #Compare les deux positions en X des deux daleks
                        if i.posY == e.posY:    #Compare les deux positions en Y des deux daleks
                            self.listFerraille.append(TasFerraille(i.posX, i.posY))  #Si oui, on créer un objet tas de feraille pour l'introduire dans la liste
                            self.listDalek.pop(self.listDalek.index(i))
                            self.listDalek.pop(self.listDalek.index(e))
                            self.docteur.creditsCosmiques += 10

        for i in self.listDalek:     #Commence une boucle dans la liste de dalek
            for q in self.listFerraille:     #Commence une boucle imbriqué dans la liste des tas de ferrailles
                if i.posX == q.posX:    #Vérifie si un des positions en X de dalek interferent avec un tas de ferraille
                    if i.posY == q.posY:    #Vérifie la même chose en position Y
                        self.listDalek.pop(self.listDalek.index(i))   #Si il ya une concordance parfaite dans les positions, on élimine le dalek courant
                        self.docteur.creditsCosmiques += 5
 
 
    def docteurEncoreEnVie(self):
        for i in self.listDalek:
            if self.docteur.posX == i.posX:
                if self.docteur.posY == i.posY:
                    return False

 
    def faireDeplacerChaqueDalek(self):
        for i in self.listDalek:
            i.avancerVersDocteur(self.docteur)
    
            
            
    def commandeDuJeu(self, commande):
        #MoveUpLeft
        if commande == ActionJeu.HautGauche:
            if self.docteur.posX > 0 and self.docteur.posY > 0:
                self.docteur.posX -=1
                self.docteur.posY -=1
            else:
                pass
        #MoveUp
        elif commande == ActionJeu.Haut:
            if self.docteur.posX > 0:
                self.docteur.posX -=1
            else:
                pass
        #MoveUpRight
        elif commande == ActionJeu.HautDroite:
            if self.docteur.posX > 0 and self.docteur.posY < self.hauteur-1:
                self.docteur.posX -=1
                self.docteur.posY +=1
            else:
                pass
        #MoveLeft
        elif commande == ActionJeu.Gauche:
            if self.docteur.posY > 0:
                self.docteur.posY -=1
            else:
                pass
        #Teleportation
        elif commande == ActionJeu.Teleportation: 
            self.docteur.teleporter(self.listDalek, self.listFerraille)
        #MoveRight
        elif commande == ActionJeu.Droite:
            if self.docteur.posY < self.hauteur-1:
                self.docteur.posY +=1
            else:
                pass
        #MoveDownLeft
        elif commande == ActionJeu.BasGauche:
            if self.docteur.posX < self.largeur-1 and self.docteur.posY > 0:
                self.docteur.posX +=1
                self.docteur.posY -=1
            else:
                pass
        #MoveDown
        elif commande == ActionJeu.Bas:
            if self.docteur.posX < self.largeur-1:
                self.docteur.posX +=1
            else:
                pass
        #MoveDownRight
        elif commande == ActionJeu.BasDroite:
            if self.docteur.posX < self.largeur-1 and self.docteur.posY < self.hauteur-1:
                self.docteur.posX +=1
                self.docteur.posY +=1
            else:
                pass
        #MoveZap
        elif commande == ActionJeu.Zap:
            self.docteur.zapper(self.listDalek)
        #MoveNull
        elif commande == ActionJeu.Rien:
            pass
        #MoveQuit
        elif commande == ActionJeu.Quitter:
            sys.exit(0)
            

###############################################################################
#                                   Vue                                       #
###############################################################################

class Vue:
    def __init__(self,Controleur):
        self.controleur = Controleur

    def clearScreen(self):
        for i in range(100):
            print(' ')  

    def afficherMenu(self):
        print()
        print('Jeu de Daleks')
        print('-------------')
        print('MENU: n (nouvelle partie)  -  m (meilleur score)  -  q (quitter)')
        touche=input('Votre choix: ')
        touche = touche.rstrip('\r')
        self.traductionToucheMenu(touche)

    def afficherPartie(self, doc, listDalek, listFerraille, largeur, hauteur, nombreEnnemi):
        print('Jeu de Daleks')
        print('-------------')
        print('Niveau ',str(self.controleur.demanderNiveau()))
        
        for x in range(largeur):
            for y in range(hauteur):
                for dal in listDalek:
                    if x == dal.posX and y == dal.posY:
                        print('D',end = '')
                        break
                else:
                    for fer in listFerraille:
                        if x == fer.posX and y == fer.posY:
                            print('#',end = '')
                            break
                    else:
                        if x == doc.posX and y == doc.posY:
                            print('W',end = '')
                        else:
                            print('-',end = '')
                if x == 1:
                    if y == hauteur-1:
                        print('   ',len(listDalek),'/',nombreEnnemi, end = '')

                if x == 2:
                    if y == hauteur-1:
                        print('   ','Credits Cosmiques: ', doc.creditsCosmiques,end = '')

                if x == 3:
                    if y == hauteur-1:
                        print('   ','Nombre de zap: ', doc.nombreZap, end = '')
            print(' ')

        print(' ')

    def traductionToucheMenu(self, touche):
        if touche == 'n':
            self.controleur.choixMenuPrincipal(ActionMenu.NouvellePartie)
        elif touche == 'm':
            self.controleur.choixMenuPrincipal(ActionMenu.MeilleurScore)
        elif touche == 'q':
            self.controleur.choixMenuPrincipal(ActionMenu.Quitter)      

    def traductionToucheJeu(self, touche):
        if touche == 'w':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Haut)
        elif touche == 'x':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Bas)
        elif touche == 'a':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Gauche)
        elif touche == 'd':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Droite)
        elif touche == 'k':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Zap)
        elif touche == 's':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Teleportation)
        elif touche == 'n':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Rien)
        elif touche == 'q':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.HautGauche)
        elif touche == 'e':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.HautDroite)
        elif touche == 'z':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.BasGauche)
        elif touche == 'c':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.BasDroite)
        elif touche == 'quit':
            self.controleur.envoyerCommandeDuJeu(ActionJeu.Quitter)


    def gameloop(self):
        while self.controleur.siPartieFini() == False:
        
        #Generer niveau au besoin et afficher le jeu
                self.controleur.genererNiveauSiBesoin()
                self.controleur.demanderInfoEtAfficherPartie()
        #Tour du Docteur    
                touche=input('Votre choix: ')
                touche = touche.rstrip('\r')
                self.traductionToucheJeu(touche)    
                #Tour des daleks  *Intelligence artificiel*
                self.controleur.demanderDeplacementDalek()
                self.controleur.demanderGestionCollision()
                #Vérifier si le Docteur est sur la meme position qu'un dalek
                if self.controleur.demanderSiDocteurEncoreEnVie() == False:
                    self.controleur.finirLaPartie()
                    
        if self.controleur.siPartieFini() == True:
            try:
                self.clearScreen()
                fo = open('D:\\results.txt', 'a')
                nom = input('Entrez votre nom: ')
                if nom == 'exit':
                    sys.exit(0)
                nom = nom.rstrip('\r')
                nb = self.controleur.demanderNombreCredits()
                ligne = (nom+ " // "+ str(nb)+ " credits cosmiques")
                fo.write(str(ligne + "\n"))
                print(ligne)
                fo.close()
            except Exception as e:
                print(e)
        

###############################################################################
#                                 Controleur                                  #
###############################################################################

class Controleur:
    def __init__(self):
        try:
            self.vue = Vue(self)
            self.vue.afficherMenu()
        except Exception as e:
            print(e)

    def choixMenuPrincipal(self, action):
        if action == ActionMenu.NouvellePartie:
            self.modele = Partie(20,30)#Creation du modele
            self.vue.gameloop()#Depart du gameloop
        elif action == ActionMenu.MeilleurScore:
            with open("D:\\results.txt") as f:
                content = f.readlines()

            print(' ')
            print(' ')
            print(' ')
            
            for l in content:
                print(l)

            input("Pesez sur une touche pour retourner au menu...")
            self.vue.clearScreen()
            self.vue.afficherMenu()
            
        elif action == ActionMenu.Quitter:
            sys.exit(0)

    def envoyerCommandeDuJeu(self, touche):
        self.modele.commandeDuJeu(touche)
            
    def siPartieFini(self):
        return self.modele.partieFini
        
    def genererNiveauSiBesoin(self):
        if not self.modele.listDalek:
            self.modele.creeNiveau()
            
    def demanderInfoEtAfficherPartie(self):
        self.vue.afficherPartie(self.modele.docteur, self.modele.listDalek, self.modele.listFerraille, self.modele.largeur, self.modele.hauteur, (self.modele.niveau*self.modele.daleksParNiveau))
    
    def demanderDeplacementDalek(self):
        self.modele.faireDeplacerChaqueDalek()

    def demanderGestionCollision(self):
        self.modele.gestionCollision()

    def demanderSiDocteurEncoreEnVie(self):
        return self.modele.docteurEncoreEnVie()

    def finirLaPartie(self):
        self.modele.partieFini = True
        
    def demanderNombreCredits(self):
        return self.modele.docteur.creditsCosmiques

    def demanderNiveau(self):
        return self.modele.niveau

###############################################################################
#                                    Main                                     #
###############################################################################
if __name__ == '__main__':
    c=Controleur()

