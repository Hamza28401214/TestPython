
#sujet1
def changeToUpperCase(text):
    result = ''
    for char in text:
       result += chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char #chr() est utilisée pour convertir un entier en une chaine de charactère , ord() fait l'inverse...
    return result
print(changeToUpperCase('Hakxkxoxoxnxn'))
print(changeToUpperCase('HHHHnnnnnaaaaa'))
print(changeToUpperCase('aaaaaaaaaaaaaaaaa'))

#########################################################################################################
#########################################################################################################""
#sujet2
#un nombre est divible par 3 si la somme de ses chiffres est divible par 3, par exemple 18 ==> 8+1=9 et 9 est div par 3
def divisible_par_3(N):
    if N in (0,3,6,9):
        return True
    if N<10:
        return False
    return divisible_par_3(sum(map(int,str(N))))
print(divisible_par_3(3000000000000000000000000000000000000000000000000000000000000000000000016723))
print(divisible_par_3(3000000000000000000000000000000000000000000000000000000000000000000000016724))
print(divisible_par_3(3000000000000000000000000000000000000000000000000000000000000000000000016725))
######################################################################################################
##################################################################################################""
#sujet3

Plateau = [[True, False, False, False],
           [False, True, True, False]]


def iterationHV(x, y):
    return [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] # (1): on a enlever la combinaision (x,y)


def _isSafe(i, j, _i, _j, l, w):
    return i >= 0 and i < l and j >= 0 and j < w and not ((i == _i) and (j == _j))


def voisinsCase(pl, case):
    # On ne peut pas considerer la case voisine à elle meme, du coup on a fait (1) mais on considere (2)
    l, w = len(pl), len(pl[0])
    voisins = []
    _i, _j = case
    for i, j in iterationHV(_i, _j):
        isSafe = _isSafe(i, j, _i, _j, l, w)
        if isSafe:
            isWanted = not pl[i][j]
            if isWanted:
                voisins.append((i, j))
    return voisins


def voisinsCases(pl, _cases):
    voisins = []
    for case in _cases:
        voisins.extend(voisinsCase(pl, case))
        voisins = list(set(voisins))
    return voisins


def accessible(pl, case):
    visited = []
    toVisit = [case]
    # (2): la case elle même est accessible à elle même
    # si on ne veut pas cette prémise à etre considerer, 
    # on remplit "toVisit" par les voisins de cette case de départ
    _accessible = []
    while len(toVisit):
        _c = toVisit.pop()
        if(not (_c in visited)):
            _voisins = voisinsCase(pl, _c)
            _accessible.extend(_voisins)
            toVisit.extend(_voisins)
            visited.append(_c)
        _accessible = list(set(_accessible))
    return _accessible


def chemin(pl, case_depart, case_arrivee):
    _accessible_depart = accessible(pl, case_depart)
    return (case_arrivee in _accessible_depart)


print(voisinsCase(Plateau, (0, 2)))
print(voisinsCases(Plateau, [(0, 0), (0, 1)]))
print(accessible(Plateau, (0, 2)))
print(chemin(Plateau, (1, 3), (1, 0)))
print(chemin(Plateau, (1, 3), (0, 1)))

