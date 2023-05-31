# main_tp2.py

from TP1.tp1 import getRandomList
from TP2.tp2 import *

print(estTrie([1]))
print(estTrie([2, 1]))

liste=[1,2,3,4,5,6,7,8,9,0]
echanger(liste,3,9)
print(liste)

liste=[7,4,8,5,9,6,5,7,4,5,7,1]
triBulles(liste)
print(liste)

print(getMin([7,4,8,5,9,1,6,5,7,4,5,7]))

print(getIndexMin([7,4,8,5,9,1,6,5,7,4,5,7]))

print(getIndexMinFrom([7,4,8,5,9,1,6,5,7,4,5,7],6))

print(triSelection([7,4,8,5,9,1,6,5,7,4,5,7]))

print(deplacerCase([ 1, 3, 3, 4, 6, 8, 2, 6, 4, 9 ],6))

print(deplacerCaseDys([1, 3, 3, 4, 6, 8, 0, 6, 4, 9], 6))

print(triInsertion([1, 3, 3, 4, 6, 8, 0, 6, 4, 9]))