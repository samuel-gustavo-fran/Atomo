class Atomo:
    def __init__(self,massa:int,numero:int,carga:int=0):
        self.massa = massa
        self.numero = numero
        self.protons = numero
        self.neutrons = massa - numero
        self.eletrons = numero - carga
    
    def de(self)-> list:
        '''
        distribução eletronica
        '''
        eletrons = self.eletrons 
        ordem = [
        ('1s', 2), ('2s', 2), ('2p', 6), ('3s', 2),
        ('3p', 6), ('4s', 2), ('3d', 10), ('4p', 6),
        ('5s', 2), ('4d', 10), ('5p', 6), ('6s', 2),
        ('4f', 14), ('5d', 10), ('6p', 6), ('7s', 2),
        ('5f', 14), ('6d', 10), ('7p', 6)
        ]
        distribuicao = []
        for subnivel, capacidade in ordem:
            if eletrons <= 0:
                break
            qtd = min(eletrons, capacidade)
            distribuicao.append(f"{subnivel}{qtd}")
            eletrons -= qtd
        return distribuicao
    def de_simple(self):
        de_simple = self.de()
        if len(self.de()) > 3 and len(self.de()) <= 5:
            de_simple[0:3] = ['[Ne]']
        elif len(self.de()) > 5 and len(self.de()) <= 8:
            de_simple[0:5] = ['[Ar]']
        elif len(self.de()) > 8 and len(self.de()) <= 11:
            de_simple[0:8] = ['[Kr]']
        elif len(self.de()) > 11 and len(self.de()) <= 15:
            de_simple[0:11] = ['[Xe]']
        elif len(self.de()) > 15 and len(self.de()) <= 19:
            de_simple[0:15] = ['[Rn]']
        else:
            raise ValueError('Distribuição invalida')
        
        return de_simple
def iselement(atomo1:Atomo,atomo2:Atomo):
    if atomo1.numero == atomo2.numero:
        return True
    else:
        return False
def isotopos(atomo1:Atomo,atomo2:Atomo):
    if atomo1.massa != atomo2.massa and iselement(atomo1,atomo2):
        return True
    else:
        return False
def isobaros(atomo1:Atomo,atomo2:Atomo):
    if atomo1.massa == atomo2.massa and not iselement(atomo1,atomo2):
        return True
    else:
        return False
def isotonos(atomo1:Atomo,atomo2:Atomo):
    if not iselement(atomo1,atomo2) and atomo1.neutrons == atomo2.neutrons:
        return True
    else:
        return False
def isoeletronico(atomo1:Atomo,atomo2:Atomo):
    if atomo1.eletrons == atomo2.eletrons:
        return True
    else:
        return False
