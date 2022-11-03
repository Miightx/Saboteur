class Pos(object):
    """Position dans l'espace de jeu"""
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Carte(object):
    """Carte du jeu SABOOTERS"""
    def __init__(self,pos,typ):
        self.pos=pos
        self.typ=typ

class Chemin(Carte):
    """Carte Chemin"""
    table=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)')]
    def __init__(self,pos,typ,up,mi,do):
        "up,mi et do determine le contenu des trois parties de la carte chemin"
        Carte.__init__(self,pos,typ)
        self.up=up
        self.mi=mi
        self.do=do

    def affiche(self,x):
        if x==0:
            print(Chemin.table[self.up],end = "")
        if x==1:
            print(Chemin.table[self.mi],end = "")
        if x==2:
            print(Chemin.table[self.do],end = "")

    
        
        
