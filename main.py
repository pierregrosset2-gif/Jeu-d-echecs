import pyxel as p,pyxel

#NOM DES PIECES : PIONS :1 , TOUR:2, CHEVAUX:3, FOU:4, REINE:5, ROI:6 
#COULEUR     NOIR:0,  BLANCS:1
class Jeu:
    def __init__(self):
        p.init(230,200)
        p.load("res.pyxres")
        self.case_roi = [0,0]
        self.case_roi_bis = [0,0]
        self.depart_selec = 0
        self.cible_selec = [96,96]
        self.apparition = 0
        self.cas_echec = []
        self.cas_echec_bis = []
        self.possibles = []
        self.apparence = []
        self.case_selec = [96,96]
        self.is_running = 0
        self.joueur = 0
        self.option = 0
        self.option_bis = 0
        self.score = 0
        self.score_bis = 0
        self.roqued = 0
        self.roqueg = 0
        self.roque_bisd = 0
        self.roque_bisg = 0
        self.echec = 0
        self.echec_bis = 0
        self.pion_chang = 0
        self.liste_case = [[(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)],[(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2)],[(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2),(0,0,2)]]
        self.liste_case_prises = []
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        
        self.upr = 0
        self.upl = 0
        self.downr = 0
        self.downl = 0
        p.run(self.update,self.draw)
        
    def possible(self,x,y,tab):
        
        self.pion_selected(x,y)
        self.possible_aux(x,y,self.apparence[0],self.apparence[1],self.apparence[3],self.apparence[2],tab,2)
        
        
    def possible_aux(self,x,y,nom,coul,att,deb,tab,taille):
        if len(tab) < taille:# att1 pour pion att gauche/ 2 pour droite 
            if coul == 0:
                if nom == 1:
                    if deb == 1: 
                        if self.liste_case[(y+48)//24][x//24][2] == 0 and self.liste_case[(y+24)//24][x//24][2] == 0:                                 
                            tab.append([x,y+48])
                                          #on enleve le double deplacement
                    if x < 168:
                        if self.liste_case[(y+24)//24][(x+24)//24][2] == 2:
                            tab.append([x+24,y+24])
                    if x > 0:
                        if self.liste_case[(y+24)//24][(x-24)//24][2] == 2:
                            tab.append([x-24,y+24])
                    if self.liste_case[(y+24)//24][x//24][2] == 0:
                        tab.append([x,y+24])
                elif nom == 2:
                    for case in range((168-x)//24):
                        if self.right == 0:
                            if self.liste_case[y//24][(x+24 + case*24)//24][2] == 0:
                                tab.append([x+24 + case*24,y])
                            elif self.liste_case[y//24][(x+24 + case*24)//24][2] == 2:
                                tab.append([x+24 + case*24,y])
                                self.right = 1
                            else:
                                self.right = 1
                    for case2 in range(x//24):
                        if self.left == 0:
                            if self.liste_case[y//24][(x-24 - case2*24)//24][2] == 0:
                                tab.append([x-24 - case2*24,y])
                            elif self.liste_case[y//24][(x-24 - case2*24)//24][2] == 2:
                                tab.append([x-24 - case2*24,y])
                                self.left = 1
                            else:
                                self.left = 1
                    for case3 in range((168-y)//24):
                        if self.down == 0:
                            if self.liste_case[(y+24 + case3*24)//24][x//24][2] == 0:
                                tab.append([x,y+24 + case3*24])
                            elif self.liste_case[(y+24 + case3*24)//24][x//24][2] == 2:
                                tab.append([x,y+24 + case3*24])
                                self.down = 1
                            else:
                                self.down = 1
                    for case4 in range(y//24):
                        if self.up == 0:
                            if self.liste_case[(y-24 - case4*24)//24][x//24][2] == 0:
                                tab.append([x,y-24 - case4*24])
                            elif self.liste_case[(y-24 - case4*24)//24][x//24][2] == 2:
                                tab.append([x,y-24 - case4*24])
                                self.up = 1
                            else:
                                self.up = 1
                elif nom == 3:
                    
                    if (x-24) >= 0 and (y-48) >= 0 and self.liste_case[(y-48)//24][(x-24)//24][2] !=1:
                        tab.append([x-24,y-48])
                    if (x+24) <= 168 and (y-48) >= 0 and self.liste_case[(y-48)//24][(x+24)//24][2] !=1:
                        tab.append([x+24,y-48])
                    if (x-48) >= 0 and (y-24) >= 0 and self.liste_case[(y-24)//24][(x-48)//24][2] != 1:
                        tab.append([x-48,y-24])
                    if (x+48) <= 168 and (y-24) >= 0 and self.liste_case[(y-24)//24][(x+48)//24][2] != 1:
                        tab.append([x+48,y-24])
                    if (x-48) >= 0 and (y+24) <= 168 and self.liste_case[(y+24)//24][(x-48)//24][2] != 1:
                        tab.append([x-48,y+24])
                    if (x+48) <= 168 and (y+24) <= 168 and self.liste_case[(y+24)//24][(x+48)//24][2] != 1:
                        tab.append([x+48,y+24])
                    if (x-24) >= 0 and (y+48) <= 168 and self.liste_case[(y+48)//24][(x-24)//24][2] != 1:
                        tab.append([x-24,y+48])
                    if (x+24) <= 168 and (y+48) <= 168 and self.liste_case[(y+48)//24][(x+24)//24][2] != 1:
                        tab.append([x+24,y+48])
                    
                   
                    
                        
                elif nom == 4:
                    
                    for case in range((168-x)//24):
                        if self.upr == 0:
                            if x+24*case < 168 and y-24*case > 0:
                                if self.liste_case[(y-24 - 24*case)//24][(x+24 + case*24)//24][2] == 0:
                                    
                                    tab.append([x+24 + case*24,y-24-24*case])
                                elif self.liste_case[(y-24-24*case)//24][(x+24 + case*24)//24][2] == 2:
                                    tab.append([x+24 + case*24,y-24-24*case])
                                    self.upr = 1
                                else:
                                    self.upr = 1
                            else:
                                self.upr = 1
                    for case2 in range((168-x)//24):
                        
                        if self.downr == 0:
                            if x+24*case2 < 168 and y+24*case2 < 168:
                                if self.liste_case[(y+24+24*case2)//24][(x+24 + case2*24)//24][2] == 0:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                elif self.liste_case[(y+24+case2*24)//24][(x+24 + case2*24)//24][2] == 2:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                    self.downr = 1
                                else:
                                    self.downr = 1
                            else:
                                self.downr = 1
                    
                    for case3 in range(x//24):
                        if self.upl == 0:
                            if x-case3*24 > 0 and y-24*case3 > 0:
                                if self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 0:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                elif self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 2:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                    self.upl = 1
                                else:
                                    self.upl = 1
                            else:
                                self.upl = 1
                    
                    for case4 in range(x//24):
                        if self.downl == 0:
                            if x-24*case4 > 0 and y+24*case4 < 168:
                                if self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 0:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                elif self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 2:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                    self.downl = 1
                                else:
                                    self.downl = 1
                            else:
                                self.downl = 1
                        
                elif nom == 5:
                    self.possible_aux(x,y,2,0,0,0,self.possibles,2)
                    for case in range((168-x)//24):
                        if self.upr == 0:
                            if x+24*case < 168 and y-24*case > 0:
                                if self.liste_case[(y-24 - 24*case)//24][(x+24 + case*24)//24][2] == 0:
                                    
                                    tab.append([x+24 + case*24,y-24-24*case])
                                elif self.liste_case[(y-24-24*case)//24][(x+24 + case*24)//24][2] == 2:
                                    tab.append([x+24 + case*24,y-24-24*case])
                                    self.upr = 1
                                else:
                                    self.upr = 1
                            else:
                                self.upr = 1
                    for case2 in range((168-x)//24):
                        
                        if self.downr == 0:
                            if x+24*case2 < 168 and y+24*case2 < 168:
                                if self.liste_case[(y+24+24*case2)//24][(x+24 + case2*24)//24][2] == 0:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                elif self.liste_case[(y+24+case2*24)//24][(x+24 + case2*24)//24][2] == 2:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                    self.downr = 1
                                else:
                                    self.downr = 1
                            else:
                                self.downr = 1
                    
                    for case3 in range(x//24):
                        if self.upl == 0:
                            if x-case3*24 > 0 and y-24*case3 > 0:
                                if self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 0:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                elif self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 2:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                    self.upl = 1
                                else:
                                    self.upl = 1
                            else:
                                self.upl = 1
                    
                    for case4 in range(x//24):
                        if self.downl == 0:
                            if x-24*case4 > 0 and y+24*case4 < 168:
                                if self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 0:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                elif self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 2:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                    self.downl = 1
                                else:
                                    self.downl = 1
                            else:
                                self.downl = 1
                else:
                    if x<168 and self.liste_case[y//24][(x+24)//24][2] != 1:
                        tab.append([x+24,y])
                    if x > 0 and self.liste_case[y//24][(x-24)//24][2] != 1:
                        tab.append([x-24,y])
                    if y < 168 and self.liste_case[(y+24)//24][x//24][2] != 1:
                        tab.append([x,y+24])
                    if y > 0 and self.liste_case[(y-24)//24][x//24][2] != 1:
                        tab.append([x,y-24])
                    if y > 0 and x < 168 and self.liste_case[(y-24)//24][(x+24)//24][2] != 1:
                        tab.append([x+24,y-24])
                    if y < 168 and  x < 168 and self.liste_case[(y+24)//24][(x+24)//24][2] != 1:
                        tab.append([x+24,y+24])
                    if y < 168 and x > 0 and self.liste_case[(y+24)//24][(x-24)//24][2] != 1:
                        tab.append([x-24,y+24])
                    if y > 0 and x > 0 and self.liste_case[(y-24)//24][(x-24)//24][2] != 1:
                        tab.append([x-24,y-24])
                    if self.roqued == 0 and self.liste_case[y//24][(x+24)//24][2] == 0 and self.liste_case[y//24][(x+48)//24][2] == 0:
                        tab.append([x+48,y])
                    if self.roqueg == 0 and self.liste_case[y//24][(x-24)//24][2] == 0 and self.liste_case[y//24][(x-48)//24][2] == 0 and self.liste_case[y//24][(x-72)//24][2] == 0:
                        tab.append([x-48,y])
                    for case in tab:
                        if self.sera_echec(0,case[0],case[1]) == True:
                            tab.remove(case)
            else:
                if nom == 1:
                    if deb == 1:
                        if self.liste_case[(y-48)//24][x//24][2] == 0 and self.liste_case[(y-24)//24][x//24][2] == 0:                                
                            tab.append([x,y-48])#premier depart de pions
                        
                    if x < 168:            
                        if self.liste_case[(y-24)//24][(x+24)//24][2] == 1:
                            tab.append([x+24,y-24])
                    if x > 0:
                        if self.liste_case[(y-24)//24][(x-24)//24][2] == 1:
                            tab.append([x-24,y-24])
                    if self.liste_case[(y-24)//24][x//24][2] == 0:
                        tab.append([x,y-24])
                elif nom == 2:
                    for case in range((168-x)//24):
                        if self.right == 0:
                            if self.liste_case[y//24][(x+24 + case*24)//24][2] == 0:
                                tab.append([x+24 + case*24,y])
                            elif self.liste_case[y//24][(x+24 + case*24)//24][2] == 1:
                                tab.append([x+24 + case*24,y])
                                self.right = 1
                            else:
                                self.right = 1
                    for case2 in range(x//24):
                        if self.left == 0:
                            if self.liste_case[y//24][(x-24 - case2*24)//24][2] == 0:
                                tab.append([x-24 - case2*24,y])
                            elif self.liste_case[y//24][(x-24 - case2*24)//24][2] == 1:
                                tab.append([x-24 - case2*24,y])
                                self.left = 1
                            else:
                                self.left = 1
                    for case3 in range((168-y)//24):
                        if self.down == 0:
                            if self.liste_case[(y+24 + case3*24)//24][x//24][2] == 0:
                                tab.append([x,y+24 + case3*24])
                            elif self.liste_case[(y+24 + case3*24)//24][x//24][2] == 1:
                                tab.append([x,y+24 + case3*24])
                                self.down = 1
                            else:
                                self.down = 1
                    for case4 in range(y//24):
                        if self.up == 0:
                            if self.liste_case[(y-24 - case4*24)//24][x//24][2] == 0:
                                tab.append([x,y-24 - case4*24])
                            elif self.liste_case[(y-24 - case4*24)//24][x//24][2] == 1:
                                tab.append([x,y-24 - case4*24])
                                self.up = 1
                            else:
                                self.up = 1
                elif nom == 3:
                    if (x-24) >= 0 and (y-48) >= 0 and self.liste_case[(y-48)//24][(x-24)//24][2] !=2:
                        tab.append([x-24,y-48])
                    if (x+24) <= 168 and (y-48) >= 0 and self.liste_case[(y-48)//24][(x+24)//24][2] !=2:
                        tab.append([x+24,y-48])
                    if (x-48) >= 0 and (y-24) >= 0 and self.liste_case[(y-24)//24][(x-48)//24][2] != 2:
                        tab.append([x-48,y-24])
                    if (x+48) <= 168 and (y-24) >= 0 and self.liste_case[(y-24)//24][(x+48)//24][2] != 2:
                        tab.append([x+48,y-24])
                    if (x-48) >= 0 and (y+24) <= 168 and self.liste_case[(y+24)//24][(x-48)//24][2] != 2:
                        tab.append([x-48,y+24])
                    if (x+48) <= 168 and (y+24) <= 168 and self.liste_case[(y+24)//24][(x+48)//24][2] != 2:
                        tab.append([x+48,y+24])
                    if (x-24) >= 0 and (y+48) <= 168 and self.liste_case[(y+48)//24][(x-24)//24][2] != 2:
                        tab.append([x-24,y+48])
                    if (x+24) <= 168 and (y+48) <= 168 and self.liste_case[(y+48)//24][(x+24)//24][2] != 2:
                        tab.append([x+24,y+48])
                   
                
                elif nom == 4:
                    
                    for case in range((168-x)//24):
                        if self.upr == 0:
                            if x+24*case < 168 and y-24*case > 0:
                                if self.liste_case[(y-24 - 24*case)//24][(x+24 + case*24)//24][2] == 0:
                                    tab.append([x+24 + case*24,y-24-24*case])
                                elif self.liste_case[(y-24-24*case)//24][(x+24 + case*24)//24][2] == 1:
                                    tab.append([x+24 + case*24,y-24-24*case])
                                    self.upr = 1
                                else:
                                    self.upr = 1
                            else:
                                self.upr = 1
                    for case2 in range((168-x)//24):
                        
                        if self.downr == 0:
                            if x+24*case2 < 168 and y+24*case2 < 168:
                                if self.liste_case[(y+24+24*case2)//24][(x+24 + case2*24)//24][2] == 0:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                elif self.liste_case[(y+24+case2*24)//24][(x+24 + case2*24)//24][2] == 1:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                    self.downr = 1
                                else:
                                    self.downr = 1
                            else:
                                self.downr = 1
                    
                    for case3 in range(x//24):
                        if self.upl == 0:
                            if x-case3*24 > 0 and y-24*case3 > 0:
                                if self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 0:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                elif self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 1:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                    self.upl = 1
                                else:
                                    self.upl = 1
                            else:
                                self.upl = 1
                    
                    for case4 in range(x//24):
                        if self.downl == 0:
                            if x-24*case4 > 0 and y+24*case4 < 168:
                                if self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 0:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                elif self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 1:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                    self.downl = 1
                                else:
                                    self.downl = 1
                            else:
                                self.downl = 1 
    
                elif nom == 5:
                    
                    self.possible_aux(x,y,2,1,0,0,self.possibles,2)
                    for case in range((168-x)//24):
                        if self.upr == 0:
                            if x+24*case < 168 and y-24*case > 0:
                                if self.liste_case[(y-24 - 24*case)//24][(x+24 + case*24)//24][2] == 0:
                                    
                                    tab.append([x+24 + case*24,y-24-24*case])
                                elif self.liste_case[(y-24-24*case)//24][(x+24 + case*24)//24][2] == 1:
                                    tab.append([x+24 + case*24,y-24-24*case])
                                    self.upr = 1
                                else:
                                    self.upr = 1
                            else:
                                self.upr = 1
                    for case2 in range((168-x)//24):
                        
                        if self.downr == 0:
                            if x+24*case2 < 168 and y+24*case2 < 168:
                                if self.liste_case[(y+24+24*case2)//24][(x+24 + case2*24)//24][2] == 0:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                elif self.liste_case[(y+24+case2*24)//24][(x+24 + case2*24)//24][2] == 1:
                                    tab.append([x+24 + case2*24,y+24+24*case2])
                                    self.downr = 1
                                else:
                                    self.downr = 1
                            else:
                                self.downr = 1
                    
                    for case3 in range(x//24):
                        if self.upl == 0:
                            if x-case3*24 > 0 and y-24*case3 > 0:
                                if self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 0:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                elif self.liste_case[(y-24 - case3*24)//24][(x-24-24*case3)//24][2] == 1:
                                    tab.append([x-24-case3*24,y-24 - case3*24])
                                    self.upl = 1
                                else:
                                    self.upl = 1
                            else:
                                self.upl = 1
                    
                    for case4 in range(x//24):
                        if self.downl == 0:
                            if x-24*case4 > 0 and y+24*case4 < 168:
                                if self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 0:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                elif self.liste_case[(y+24 + case4*24)//24][(x-24-24*case4)//24][2] == 1:
                                    tab.append([x-24-24*case4,y+24 + case4*24])
                                    self.downl = 1
                                else:
                                    self.downl = 1
                            else:
                                self.downl = 1
                    
                else:
                    if x<168 and self.liste_case[y//24][(x+24)//24][2] != 2:
                        tab.append([x+24,y])
                    if x > 0 and self.liste_case[y//24][(x-24)//24][2] != 2:
                        tab.append([x-24,y])
                    if y < 168 and self.liste_case[(y+24)//24][x//24][2] != 2:
                        tab.append([x,y+24])
                    if y > 0 and self.liste_case[(y-24)//24][x//24][2] != 2:
                        tab.append([x,y-24])
                    if y > 0 and x < 168 and self.liste_case[(y-24)//24][(x+24)//24][2] != 2:
                        tab.append([x+24,y-24])
                    if y < 168 and  x < 168 and self.liste_case[(y+24)//24][(x+24)//24][2] != 2:
                        tab.append([x+24,y+24])
                    if y < 168 and x > 0 and self.liste_case[(y+24)//24][(x-24)//24][2] != 2:
                        tab.append([x-24,y+24])
                    if y > 0 and x > 0 and self.liste_case[(y-24)//24][(x-24)//24][2] != 2:
                        tab.append([x-24,y-24])
                    if self.roque_bisd == 0 and self.liste_case[y//24][(x+24)//24][2] == 0 and self.liste_case[y//24][(x+48)//24][2] == 0:
                        tab.append([x+48,y])
                    if self.roque_bisg == 0 and self.liste_case[y//24][(x-24)//24][2] == 0 and self.liste_case[y//24][(x-48)//24][2] == 0 and self.liste_case[y//24][(x-72)//24][2] == 0:
                        tab.append([x-48,y])
                    
    def mouvement(self,x,y):
        if self.depart_selec == 1:
            
            if p.btnp(p.KEY_RETURN):
                self.joueur += 1
                for case in self.possibles:
                    if x == case[0] and y == case[1]:
                        
                        n = len(self.apparence)
                        if n != 0:
                            if self.apparence[1] == 0:
                                for pion in liste_pions.pions_blancs:
                                    if pion.x == x and pion.y == y:
                                        self.score += pion.score
                                        liste_pions.pions_blancs.remove(pion)
                            else:
                                for pion in liste_pions.pions_noirs:
                                    if pion.x == x and pion.y == y:
                                        self.score_bis += pion.score
                                        liste_pions.pions_noirs.remove(pion)
                        
                        for pions in liste_pions.pions_noirs:
                            if pions.x == x-48 and pions.y == y and pions.nom == 6 and self.roqued == 0 and pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                self.roqued = 1
                                self.roqueg = 1
                                for pion in liste_pions.pions_noirs:
                                    if pion.x == 168 and pion.y == 0:
                                        pion.x -= 48
                                        pion.y = 0
                                        self.liste_case[0][7] = (168,0,0)
                                        self.liste_case[0][5] = (120,0,1)
                            elif pions.x == x+48 and pions.y == y and pions.nom == 6 and self.roqueg == 0 and pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                self.roqued = 1
                                self.roqueg = 1
                                for pion in liste_pions.pions_noirs:
                                    if pion.x == 0 and pion.y == 0:
                                        pion.x += 72
                                        pion.y = 0
                                        self.liste_case[0][0] = (0,0,0)
                                        self.liste_case[0][3] = (72,0,1)
                            if pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                pions.x = x
                                pions.y = y
                                
                                self.depart_selec = 0
                                self.liste_case[y//24][x//24] = (x,y,1)
                                a = self.case_selec[0]
                                b = self.case_selec[1]
                                
                                self.liste_case[b//24][a//24] = (a,b,0)
                                
                                pions.deb = 0
                                self.up = 0
                                self.down = 0
                                self.left = 0
                                self.right = 0
                                self.upr = 0
                                self.upl = 0
                                self.downr = 0
                                self.downl = 0
                        for pions in liste_pions.pions_blancs:
                            if pions.x == x-48 and pions.y == y and pions.nom == 6 and self.roque_bisgd == 0 and pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                self.roque_bisd = 1
                                self.roque_bisg = 1
                                for pion in liste_pions.pions_blancs:
                                    if pion.x == 168 and pion.y == 168:
                                        pion.x -= 48
                                        pion.y = 168
                                        self.liste_case[7][7] = (168,168,0)
                                        self.liste_case[7][5] = (120,168,1)
                            elif pions.x == x+48 and pions.y == y and pions.nom == 6 and self.roque_bisg == 0 and pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                self.roque_bisd = 1
                                self.roque_bisg = 1
                                for pion in liste_pions.pions_blancs:
                                    if pion.x == 0 and pion.y == 168:
                                        pion.x += 72
                                        pion.y = 168
                                        self.liste_case[7][0] = (0,168,0)
                                        self.liste_case[7][3] = (72,168,1)
                            if pions.x == self.case_selec[0] and pions.y == self.case_selec[1]:
                                pions.x = x
                                pions.y = y
                                
                                self.depart_selec = 0
                                self.liste_case[y//24][x//24] = (x,y,2)
                                a = self.case_selec[0]
                                b = self.case_selec[1]
                                self.liste_case[b//24][a//24] = (a,b,0)   
                                pions.deb = 0
                                self.up = 0
                                self.down = 0
                                self.left = 0
                                self.right = 0
                                self.upr = 0
                                self.upl = 0
                                self.downr = 0
                                self.downl = 0
                        self.possibles = []
                        for pion in liste_pions.pions_noirs:
                            if pion.nom == 6:
                                self.est_echec(0,pion.x,pion.y)
                        for pions in liste_pions.pions_blancs:
                            if pions.nom == 6:
                                self.est_echec(1,pions.x,pions.y)
                       
                        
    def roque_dispo(self):
        if self.liste_case[0][4][2] != 1:
            self.roqued = 1
            self.roqueg = 1
        if self.liste_case[0][0][2] != 1:  
            self.roqueg = 1
        if self.liste_case[0][7][2] != 1:
            self.roqued = 1
        
        if self.liste_case[7][4][2] != 2:
            self.roque_bisd = 1
            self.roque_bisg = 1
        if self.liste_case[7][0][2] != 2:  
            self.roque_bisg = 1
        if self.liste_case[7][7][2] != 2:
            self.roque_bisd = 1
    
    def pion_selected(self,x,y):
        for pions in liste_pions.pions_noirs:
            if pions.x == x and pions.y == y:
                self.apparence = [pions.nom,pions.couleur,pions.deb,pions.att]
                
        for pions in liste_pions.pions_blancs:
            if pions.x == x and pions.y == y:
                self.apparence = [pions.nom,pions.couleur,pions.deb,pions.att]
                
        
        
  
    def est_echec(self,coul,x,y):
        if coul == 0:
            for pion in liste_pions.pions_blancs:
                self.possible_aux(pion.x,pion.y,pion.nom,pion.couleur,pion.att,pion.deb,self.cas_echec,100)
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
                self.upr = 0
                self.upl = 0
                self.downr = 0
                self.downl = 0
            
            for case in self.cas_echec:
                if x == case[0] and y == case[1]:
                    self.echec = 1
                    return True
            self.cas_echec = []
            self.echec = 0
        
        else:
            for pion in liste_pions.pions_noirs:
                self.possible_aux(pion.x,pion.y,pion.nom,pion.couleur,pion.att,pion.deb,self.cas_echec,100)
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
                self.upr = 0
                self.upl = 0
                self.downr = 0
                self.downl = 0
            
            for case in self.cas_echec:
                if x == case[0] and y == case[1]:
                    self.echec_bis = 1
                    return True
            self.cas_echec = []
            self.echec_bis = 0
    
    def sera_echec(self,coul,x,y):
        if coul == 0:
            for pion in liste_pions.pions_blancs:
                self.possible_aux(pion.x,pion.y,pion.nom,pion.couleur,pion.att,pion.deb,self.cas_echec_bis,100)
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
                self.upr = 0
                self.upl = 0
                self.downr = 0
                self.downl = 0
            
            for case in self.cas_echec_bis:
                if x == case[0] and y == case[1]:
                    
                    return True
            self.cas_echec_bis = []
            return False
        
        else:
            for pion in liste_pions.pions_noirs:
                self.possible_aux(pion.x,pion.y,pion.nom,pion.couleur,pion.att,pion.deb,self.cas_echec_bis,100)
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
                self.upr = 0
                self.upl = 0
                self.downr = 0
                self.downl = 0
            
            for case in self.cas_echec_bis:
                if x == case[0] and y == case[1]:
                    
                    return True
            self.cas_echec_bis = []
            return False
     
    def pion_change(self):
        for pion in liste_pions.pions_noirs:
            if pion.nom == 1 and pion.y == 168:
                self.pion_chang = 1
                if p.btnp(p.KEY_A):
                    pion.nom = 5
                    self.pion_chang = 0
                    self.est_echec(0,self.case_roi[0],self.case_roi[1])
                elif p.btnp(p.KEY_B):
                    pion.nom = 2
                    self.pion_chang = 0
                    self.est_echec(0,self.case_roi[0],self.case_roi[1])
                elif p.btnp(p.KEY_C):
                    pion.nom = 3
                    self.pion_chang = 0
                    self.est_echec(0,self.case_roi[0],self.case_roi[1])
                elif p.btnp(p.KEY_D):
                    pion.nom = 4
                    self.pion_chang = 0
                    self.est_echec(0,self.case_roi[0],self.case_roi[1])
                
        for pions in liste_pions.pions_blancs:
            if pions.nom == 1 and pions.y == 0:
                self.pion_chang = 1
                if p.btnp(p.KEY_A):
                    pions.nom = 5
                    self.pion_chang = 0
                    self.est_echec(1,self.case_roi_bis[0],self.case_roi_bis[1])
                elif p.btnp(p.KEY_B):
                    pions.nom = 2
                    self.pion_chang = 0
                    self.est_echec(1,self.case_roi_bis[0],self.case_roi_bis[1])
                elif p.btnp(p.KEY_C):
                    pions.nom = 3
                    self.pion_chang = 0
                    self.est_echec(1,self.case_roi_bis[0],self.case_roi_bis[1])
                elif p.btnp(p.KEY_D):
                    pions.nom = 4
                    self.pion_chang = 0
                    self.est_echec(1,self.case_roi_bis[0],self.case_roi_bis[1])
    
    def case_rois(self,coul):
        if coul == 0:
            for pion in liste_pions.pions_noirs:
                if pion.nom == 6:
                    self.case_roi[0] = pion.x
                    self.case_roi[1] = pion.y
        elif coul == 1:    
            for pion in liste_pions.pions_blancs:
                if pion.nom == 6:
                    self.case_roi_bis[0] = pion.x
                    self.case_roi_bis[1] = pion.y
    
    
    def est_cliquee(self,x,y):
        return p.mouse_x > x and p.mouse_x < x+24 and p.mouse_y > y and p.mouse_y < y+24 and p.btnp(p.MOUSE_BUTTON_LEFT)
        
    
    def creation_pions(self,coul):
        if coul == 0:
            for i in range(8):
                liste_pions.pions_noirs.append(Pieces(24*i,24,0,1))
        else:
            for i in range(8):
                liste_pions.pions_blancs.append(Pieces(24*i,144,1,1))
        
    def creation_tours(self,coul):
        if coul == 0:
            for z in range(2):
                liste_pions.pions_noirs.append(Pieces(168*z,0,0,2))
        else:
            for y in range(2):
                liste_pions.pions_blancs.append(Pieces(168*y,168,1,2))
                
    def creation_chevaux(self,coul):
        if coul == 0:
            for i in range(2):
                liste_pions.pions_noirs.append(Pieces(120*i+24,0,0,3))
        else:
            for i in range(2):
                liste_pions.pions_blancs.append(Pieces(120*i+24,168,1,3))
                
    def creation_fous(self,coul):
        if coul == 0:
            for i in range(2):
                liste_pions.pions_noirs.append(Pieces(72*i+48,0,0,4))
        else:
            for i in range(2):
                liste_pions.pions_blancs.append(Pieces(72*i+48,168,1,4))
                
    def creation_reines(self,coul):
        if coul == 0:
            liste_pions.pions_noirs.append(Pieces(72,0,0,5))
        else:
            liste_pions.pions_blancs.append(Pieces(72,168,1,5))
    
    def creation_roi(self,coul):
        if coul == 0:
            liste_pions.pions_noirs.append(Pieces(96,0,0,6))
        else:
            liste_pions.pions_blancs.append(Pieces(96,168,1,6))
        
    def creation_ensemble(self):
        self.creation_pions(0)
        self.creation_pions(1)
        self.creation_tours(0)
        self.creation_tours(1)
        self.creation_fous(0)
        self.creation_fous(1)
        self.creation_chevaux(0)
        self.creation_chevaux(1)
        self.creation_reines(0)
        self.creation_reines(1)
        self.creation_roi(0)
        self.creation_roi(1)
    
    
    def liste_cases_prises(self):
        for pion in liste_pions.pions_noirs:
            if len(self.liste_case_prises) < 32:
                self.liste_case_prises.append([pion.x,pion.y,0])
        for pion in liste_pions.pions_blancs:
            if len(self.liste_case_prises) < 32:
                self.liste_case_prises.append([pion.x,pion.y,0])
    
        
    def cord_cases(self):
        if self.liste_case[7][7][1] == 0:
            for i in range(8):
                for k in range(8):
                    self.liste_case[i][k] = (24*k,24*i,0)
    
    def est_sur_case(self,x,y):
        if self.liste_case[x//24][y//24] == (x,y,1):
            return True
        else:
            return False
            
    def selection_case(self):
        if self.depart_selec == 1:
            if p.btnp(p.KEY_RIGHT):
                if self.cible_selec[0] < 168:
                    self.cible_selec[0] += 24
            if p.btnp(p.KEY_LEFT):
                if self.cible_selec[0] > 0:
                    self.cible_selec[0] -= 24
            if p.btnp(p.KEY_UP):
                if self.cible_selec[1] > 0:
                    self.cible_selec[1] -= 24
            if p.btnp(p.KEY_DOWN):
                if self.cible_selec[1] < 168:
                    self.cible_selec[1] += 24
            
            if p.btnp(p.KEY_L):
                
                self.possibles = []
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
                self.upr = 0
                self.upl = 0
                self.downr = 0
                self.downl = 0
                self.depart_selec = 0
                
        else:
            if p.btnp(p.KEY_L) and self.liste_case[self.case_selec[1]//24][self.case_selec[0]//24][2] !=0:
                self.cible_selec[0] = self.case_selec[0]
                self.cible_selec[1] = self.case_selec[1]
                self.depart_selec = 1
            if p.btnp(p.KEY_RIGHT):
                self.possibles = []
                if self.case_selec[0] < 168:
                    self.case_selec[0] += 24
            if p.btnp(p.KEY_LEFT):
                self.possibles = []
                if self.case_selec[0] > 0:
                    self.case_selec[0] -= 24
            if p.btnp(p.KEY_UP):
                self.possibles = []
                if self.case_selec[1] > 0:
                    self.case_selec[1] -= 24
            if p.btnp(p.KEY_DOWN):
                self.possibles = []
                if self.case_selec[1] < 168:
                    self.case_selec[1] += 24
                
        
    def update(self):
        if p.btnp(p.KEY_P):
            p.quit()
        
        if self.is_running == 2:
            if p.mouse_x > 10 and p.mouse_x < 27 and p.mouse_y > 160 and p.mouse_y < 177 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 0
        if self.is_running == 0:
            if p.mouse_x > 63 and p.mouse_x < 129 and p.mouse_y < 123 and p.mouse_y > 100 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 1
            if p.mouse_x > 54 and p.mouse_x < 141 and p.mouse_y > 159 and p.mouse_y < 176 and p.btnp(p.MOUSE_BUTTON_LEFT):
                self.is_running = 2
        if self.is_running == 1: 
            self.case_rois(1)
            self.case_rois(0)
            self.selection_case()
            self.liste_cases_prises()
            self.roque_dispo()
            if self.apparition == 0:
                self.creation_ensemble()
                self.apparition = 1
             
            self.pion_change()
            if self.depart_selec == 1:
               
                self.possible(self.case_selec[0],self.case_selec[1],self.possibles)
            self.mouvement(self.cible_selec[0],self.cible_selec[1])
            
    def draw(self):
        
        p.cls(0)
        if self.is_running == 2:
            p.text(80,10,"COMMANDES",10)
            p.text(10,30,"Pour se deplacer de cases en cases : FLECHES",15)
            p.text(10,50,"Verouillage et deverouillage d'une case : L",15)
            p.text(10,70,"Pour deplacer un pion, verouillez la case et",15)
            p.text(10,77,"ENTREE quand vous etes sur la case voulue",15)
            p.text(80,105,"OPTIONS",10)
            p.text(10,120,"INDICATEUR DES COUPS POSSIBLES :",15)
            p.text(10,140,"AFFICHAGE DU SCORE :",15)
            
            if self.option == 0:
                p.blt(140,113,0,136,8,16,16,0)
                if p.mouse_x > 140 and p.mouse_x < 157 and p.mouse_y > 113 and p.mouse_y < 130 and p.btnp(p.MOUSE_BUTTON_LEFT):
                    self.option = 1
            else:
                p.blt(140,113,0,136,32,16,16,0)
                if p.mouse_x > 140 and p.mouse_x < 157 and p.mouse_y > 113 and p.mouse_y < 130 and p.btnp(p.MOUSE_BUTTON_LEFT):
                    self.option = 0
                
            if self.option_bis == 0:
                p.blt(95,133,0,136,8,16,16,0)
                if p.mouse_x > 95 and p.mouse_x < 112 and p.mouse_y > 133 and p.mouse_y < 150 and p.btnp(p.MOUSE_BUTTON_LEFT):
                    self.option_bis = 1
            else:
                p.blt(95,133,0,136,32,16,16,0)
                if p.mouse_x > 95 and p.mouse_x < 112 and p.mouse_y > 133 and p.mouse_y < 150 and p.btnp(p.MOUSE_BUTTON_LEFT):
                    self.option_bis = 0
                
            p.blt(p.mouse_x,p.mouse_y,0,93,45,6,6,0)
            p.blt(10,170,0,103,42,16,16,0)
        if self.is_running == 0:
            p.cls(1)
            p.blt(p.mouse_x,p.mouse_y,0,93,45,6,6,0)
            p.blt(65,160,0,78,150,85,16,0)
            p.blt(50,30,0,27,187,117,34,0)
            p.blt(73,100,0,77,125,65,22,0)
            
        if self.is_running == 1:
            for i in range(8):
                p.text(195,10+24*i,f"{i+1}",11)
            p.text(10+24*0,195,"A",11)
            p.text(10+24*1,195,"B",11)
            p.text(10+24*2,195,"C",11)
            p.text(10+24*3,195,"D",11)
            p.text(10+24*4,195,"E",11)
            p.text(10+24*5,195,"F",11)
            p.text(10+24*6,195,"G",11)
            p.text(10+24*7,195,"H",11)
    
            if self.pion_chang == 1:
                p.text(193,70,"Reine: a",10)
                p.text(193,80,"Tour: b",10)
                p.text(193,90,"Cheval: c",10)
                p.text(193,100,"Fou : d",10)
            if self.echec == 1:
                p.text(196,45,"ECHEC",2)
            if self.echec_bis == 1:
                p.text(196,154,"ECHEC",2)
            if self.joueur % 2 == 0:
                p.blt(200,20,0,104,19,16,10,0)
            else:
                p.blt(200,164,0,104,19,16,10,0)
            p.bltm(0,0,0,0,0,192,192)
            p.blt(p.mouse_x,p.mouse_y,0,45,30,5,5,0)
            if self.depart_selec == 0:
                p.blt(self.case_selec[0],self.case_selec[1],0,208,80,24,24,0)
            if self.depart_selec == 1:
                if self.option == 0:
                    for poss in self.possibles:
                        p.blt(poss[0],poss[1],0,80,72,24,24,0)
                p.blt(self.cible_selec[0],self.cible_selec[1],0,208,112,24,24,0)
                p.blt(self.case_selec[0],self.case_selec[1],0,208,48,24,24,0)
            if self.option_bis == 0:
                p.text(210,35,str(self.score),10)
                p.text(210,177,str(self.score_bis),10)        
            
            for pion in liste_pions.pions_noirs:
                if pion.nom == 1:
                    p.blt(pion.x,pion.y,0,0,40,24,24,0)
                elif pion.nom == 2:
                    p.blt(pion.x,pion.y,0,0,64,24,24,0)
                elif pion.nom == 3:
                    p.blt(pion.x,pion.y,0,0,88,24,24,0)
                elif pion.nom == 4:
                    p.blt(pion.x,pion.y,0,0,112,24,24,0)
                elif pion.nom == 5:
                    p.blt(pion.x,pion.y,0,0,160,24,24,0) 
                elif pion.nom == 6:
                    p.blt(pion.x,pion.y,0,0,136,24,24,0)
                
            for pion in liste_pions.pions_blancs:
                if pion.nom == 1:
                    p.blt(pion.x,pion.y,0,48,40,24,24,0)
                elif pion.nom == 2:
                    p.blt(pion.x,pion.y,0,24,40,24,24,0)
                elif pion.nom == 3:
                    p.blt(pion.x,pion.y,0,24,64,24,24,0)
                elif pion.nom == 4:
                    p.blt(pion.x,pion.y,0,24,88,24,24,0)
                elif pion.nom == 5:
                    p.blt(pion.x,pion.y,0,24,136,24,24,0) 
                elif pion.nom == 6:
                    p.blt(pion.x,pion.y,0,24,112,24,24,0)
        
        
class Pieces:
    def __init__(self,x,y,coul,nom):
        self.x = x
        self.y = y
        self.couleur = coul
        self.nom = nom
        self.deb = 1
        self.att = 0
        if self.nom == 1:
            self.score = 1
        elif self.nom == 2:
            self.score = 5
        elif self.nom == 3:
            self.score = 3
        elif self.nom == 4:
            self.score = 3
        elif self.nom == 5:
            self.score = 8

        
class Liste_pions:
    def __init__(self):
        self.pions_noirs = [] 
        self.pions_blancs = []
        
        
        
        
        
                
liste_pions = Liste_pions()        
Jeu()
