import class_Sab as sb
import numpy as np

pos1=sb.Pos(0,0)
pos2=sb.Pos(1,1)
deck=[]

carte=sb.Cheminrand(pos1,0)
deck.append(carte)
carte=sb.Cheminrand(pos2,0)
deck.append(carte)

plateau=[[sb.Casevide for x in range(9)] for x in range(5)]
for i in range(0,len(deck)):
    plateau[deck[i].pos.x][deck[i].pos.y]=deck[i]

for i in range(0,len(plateau)):
    for x in range(0,3):
        for j in range(0,len(plateau[0])):
            plateau[i][j].affiche(x)
        print("")



