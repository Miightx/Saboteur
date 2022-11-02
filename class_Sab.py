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

    table=[('(   )'),('( | )'),('(---)'),('( x )'),('(-+ )'),('( +-)')]
