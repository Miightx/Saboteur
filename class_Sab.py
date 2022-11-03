class pos(object):
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
    def __init__(self,pos,typ,up,mi,do):
        "up,mi et do determine le contenu des trois parties de la carte chemin"
        table=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-'),('(-+ )'),('( +-)')]
        Carte.__init__(self,pos,typ)
        self.up=up
        self.mi=mi
        self.do=do
        
        
