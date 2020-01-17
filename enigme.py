from collections import Counter

def enigmeHarryPotter(fiole):
    """ 
        Résolution de l'énigme du premier tome de Harry Potter
        pour accéder à la pièrre philosophale.
        Pour ce faire, chacune des 7 boîtes peut contenir 4
        différent potions (poison, vin, avancer, reculer) codés par 0, 1, 2, 3.
    """
    
    if fiole[1] != fiole[5]: return False
    if fiole[5] == 0: return False
    if fiole[2] == 0: return False
    if fiole[0] == fiole[6] : return False
    if fiole[0] == 2: return False
    if fiole[6] == 2: return False
    
    f = Counter(fiole)
    if f[0] != 3: return False
    if f[1] != 2: return False
    if f[2] != 1: return False
    if f[3] != 1: return False
    
    for i in range(1, 7):
        if fiole[i] == 1 and fiole[i-1] != 0:
            return False
    return True

resultat = []
for j in range(4**6):
    l = [(j % (4**i)) // (4**(i-1)) for i in range(1,7)]
    l.insert(5, l[1])
    if enigmeHarryPotter(l):
        resultat.append(l)
print(resultat)

