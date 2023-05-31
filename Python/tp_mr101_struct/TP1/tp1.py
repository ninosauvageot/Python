from random import *


def getRandomList(taille: int, mini: int, maxi: int) -> list:
    liste = []
    for i in range(taille):
        liste.append(randint(mini, maxi))
    return liste


def compter(lst: list, elmt: int, ) -> int:
    compteur = 0
    for i in range(len(lst)):
        if lst[i] == elmt:
            compteur += 1
    return compteur


def contient(lst: list, n: int) -> bool:
    res = False
    for i in range(len(lst)):
        if n == lst[i]:
            res = True
    return res


def firstIndexOf(lst: list, n: int) -> int:
    res = -1
    for i in range(len(lst)):
        if n == lst[i] and res == -1:
            res = i
    return res


def lastIndexOf(lst: list, n: int) -> int:
    res = -1
    for i in range(len(lst)):
        if n == lst[i]:
            res = i
    return res


def nthIndexOf(lst: list, n: int, elmt: int) -> int:
    res = -1
    for i in range(len(lst)):
        if elmt == lst[i]:
            n -= 1
            if n == 0:
                res = i
    return res


def creerListeSansDoublon(lst: list) -> list:
    lst2 = []
    for i in range(len(lst)):
        if lst[i] not in lst2:
            lst2.append(lst[i])
    return lst2


def supprimerDoublons(lst: list) -> None:
    lst2 = []
    for i in range(len(lst)):
        if lst[i] not in lst2:
            lst2.append(lst[i])
    lst[:] = lst2


def enumerer(lst: list) -> None:
    nombres = creerListeSansDoublon(lst)

    for n in nombres:
        i = 1
        pos = 0
        positions = []
        while pos != -1:
            pos = nthIndexOf(lst, i, n)
            if pos != -1:
                positions.append(pos)
                i += 1

        print(f'Position(s) du {n} : {positions}')

