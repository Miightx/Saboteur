import class_Sab as sb
import numpy as np

def affichePlateau(deck):
    #creation du plateau
    plateau=[[sb.Casevide for x in range(9)] for x in range(5)]
    for i in range(0,len(deck)):
        plateau[deck[i].pos.x][deck[i].pos.y]=deck[i]
    
    #affiche de la premiere ligne
    for i in range(0,10):
        if i==0 :
            print(" |",end = "")
        else:
            print(" ",i-1," ",end = "")
    print("")

        #affichege de la deuxieme ligne
    for i in range(0,10):
        if i==0 :
            print("-+",end = "")
        else:
            print("-----",end = "")
    print("")

    for i in range(0,len(plateau)):
        for x in range(0,3):
            if x==1:
                print(i,end = "")
                print("|",end = "")
            else:
                print(" |",end = "")
            for j in range(0,len(plateau[0])):
                plateau[i][j].affiche(x)
            print("")

    #affichege de la derniere ligne
    for i in range(0,10):
        if i==0 :
            print("-+",end = "")
        else:
            print("-----",end = "")
    print("")