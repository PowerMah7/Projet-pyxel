#Mahé de Berranger 1G2
#Samuel Brones 1G1
#Herault Adel 1G1
#kiyan Laranjeira 1G1
import pyxel,random
global var_nuage,coord,coord_x,skin,map_x,map_y,sol_color,map_id,Saut,jumping
jumping=0
map_id=0
map_y=0
map_x=0
dash=2
var_nuage=0
coord=0
coord_x=6
skin=0
Saut=False
def sol():
    for sol in range(0,300,16):
        pyxel.blt(sol,49,1,0,0,16,16,0)
        pyxel.blt(sol,65,2,0,0,16,16,0)
        pyxel.blt(32,32,1,32,0,16,16,0)
            
def nuage(y):
    global coord,coord_x
    if coord>=150:
        coord=0
    coord=coord+1
    if coord_x>=150:
        coord_x=0
    coord_x=coord_x+2
    pyxel.blt(coord,y,1,48,0,16,16,0)
    pyxel.blt(coord_x,y+8,1,48,0,16,16,0)
        
class App:
    def __init__(self):
        #initialisation de la fenêtre:dimension 160*80 et titre
        pyxel.init(160, 80, title="Mon premier jeu Pyxel")
        #chargement des medias (dessins,musiques,sons)
        pyxel.load("media.pyxres")
        #les methodes update() et draw() sont executables en boucles
        #30 fois par seconde
        pyxel.music(7)
        pyxel.playm(7,1,True)
        self.player_x = 5
        self.player_y = 41
        self.player_speed = 2
        self.jump_speed = 0
        self.gravity = 0.4
        #Music made by Adel Herault (LE DJ)
        pyxel.run(self.update, self.draw)
       

       
        
        

    def update(self):
        global x,y,dash,skin,map_x,map_id,Saut,jumping
        if pyxel.btnp(pyxel.KEY_Q):
            #On quitte si la touche Q (Qwerty) est pressee
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_y<=50:
            skin=0
            if jumping==1:
                skin=32
            self.player_x=self.player_x+self.player_speed
            if self.player_x>=150:
                map_id += 1
                self.player_x=5
                map_x=map_x+160
                dash=2
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_y<=50:
            skin=16
            if jumping==1:
                skin=48
            self.player_x-=self.player_speed
            if self.player_x<=2:
                self.player_x=2
                if map_x!=0:
                    map_id -= 1
                    map_x=map_x-160
                    self.player_x=145
                    
        if pyxel.btn(pyxel.KEY_UP) and Saut==True:
            jumping=1
            self.jump_speed = -4
            Saut=False
        self.jump_speed += self.gravity
        self.player_y += self.jump_speed
        
        for i in range(6,9):
            if pyxel.pget(self.player_x + i, self.player_y + 16) == 11 or pyxel.pget(self.player_x + i, self.player_y + 16)==9 or pyxel.pget(self.player_x + i, self.player_y + 16)==6:
                jumping=0
                self.jump_speed = 0
                self.gravity = 0
                self.player_y=int(self.player_y)  
                Saut=True
            if pyxel.pget(self.player_x + i, self.player_y + 16) != 11 and pyxel.pget(self.player_x + i, self.player_y + 16)!=9 and pyxel.pget(self.player_x + i, self.player_y + 16)!=6:
                self.gravity = 0.4
                Saut=False
        
        if pyxel.btnp(pyxel.KEY_SPACE):
            if dash >= 1:
                if skin==0:
                    self.player_x+=30
                if skin==16:
                    self.player_x-=30
                    if self.player_x>=156:
                        self.player_x=-20
                        dash=2
            dash=dash-1
        if pyxel.btnp(pyxel.KEY_P):
            pyxel.blt(self.player_x,self.player_y,1,0,0,16,16,0)
            
        if self.player_y>=62:
            map_id=0
            map_y=0
            map_x=0
            dash=2
            var_nuage=0
            coord=0
            coord_x=6
            skin=0
            self.player_x = 5
            self.player_y = 41
            self.player_speed = 2
            self.jump_speed = 0
            self.gravity = 0.4
            jumping=0


        
    def draw(self):
        #sol()
        pyxel.cls(0)
        pyxel.bltm(0,0,0,map_x,map_y,160,80)
        pyxel.blt(self.player_x,self.player_y,0,skin,0,16,16,0)
        nuage(8)
        
            
            
App()