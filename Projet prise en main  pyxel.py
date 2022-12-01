#Mahé de Berranger 1ere2
#Samuel Brones 1G1
#Herault Adel 1G1
#kiyan Laranjeira 1G1
import pyxel
global x,y,dash
x=5
y=44
dash=2
class App:
    def __init__(self):
        #initialisation de la fenêtre:dimension 160*80 et titre
        pyxel.init(160, 80, title="Mon premier jeu Pyxel")
        #chargement des medias (dessins,musiques,sons)
        pyxel.load("media.pyxres")
        #les methodes update() et draw() sont executables en boucles
        #30 fois par seconde
        pyxel.music(0)
        pyxel.playm(0,1,True)
        #Music made by Adel Herault (LE DJ)
        pyxel.run(self.update, self.draw)

    def update(self):
        global x,y,dash
        if pyxel.btnp(pyxel.KEY_Q):
            #On quitte si la touche Q (Qwerty) est pressee
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT):
            x=x+2
            if x>=156:
                x=-2
                dash=2
        if pyxel.btn(pyxel.KEY_LEFT):
            x=x-2
            if x<=-2:
                x=-2
        if pyxel.btn(pyxel.KEY_UP):
            y=y-2
        if pyxel.btn(pyxel.KEY_DOWN):
            y=y+2
            if y>=44:
                y=44
                
        if pyxel.btnp(pyxel.KEY_SPACE):
            if dash >= 1:
                x=x+30
                if x>=156:
                    x=-20
                    dash=2
            dash=dash-1
            
            
            
    def draw(self):
        pyxel.cls(0)
        for sol in range(0,300,16):
            pyxel.blt(sol,49,1,0,0,16,16,0)
            pyxel.blt(sol,65,2,0,0,16,16,0)
        pyxel.blt(x,y,0,0,0,16,16,0)
        
        
        
        
            
App()