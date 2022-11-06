import class_Sab as sb
import numpy as np

deck=[]


deck.append(sb.Cheminrand(sb.Pos(4,2),0))

deck.append(sb.Cheminrand(sb.Pos(1,1),0))

plateau=[[sb.Casevide for x in range(9)] for x in range(5)]
for i in range(0,len(deck)):
    plateau[deck[i].pos.x][deck[i].pos.y]=deck[i]

for i in range(0,len(plateau)):
    for x in range(0,3):
        for j in range(0,len(plateau[0])):
            plateau[i][j].affiche(x)
        print("")



