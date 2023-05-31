# main_tp1.py
from TP1.tp1 import *

for i in range(5):
    print(getRandomList(10, -20, 20))

liste=getRandomList(10, -5, 5)
print(compter(liste, 0))
print(compter(liste, 10))

print(contient([7,8,5,4,5,8,4,8,7,1,2,3,6,4,8,9,5],4))

print(firstIndexOf([7,8,5,4,8],8))

print(lastIndexOf([7,8,5,4,8],8))

print(nthIndexOf([7,8,5,8,7,8],2,8))

print(creerListeSansDoublon([7,8,5,4,5,8,4,8,7,1,2,3,6,4,8,9,5]))

liste = [5, 2, 4, 2, 7, 5, 6, 2, 7, 4, 5, 7, 9]
supprimerDoublons(liste)
print(liste)

enumerer([5, 2, 4, 2, 7, 5, 6, 2, 7, 4, 5, 7, 9])
