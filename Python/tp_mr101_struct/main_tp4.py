# main_tp4.py
from TP4.tp4 import *
from random import *
def test_getRegularArray2D() -> None :
    lst = getRegularArray2D(4, 5, -10, 10)
    print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")
    return None
test_getRegularArray2D()

def test_getMinMax() -> None:
    for i in range(5):
        lst = getRegularArray2D(randint(1,5),randint(1,5), -10, 10)
        print(f"Valeur minimale de {lst} : Min =",getMin(lst),"max = ",getMax(lst))

test_getMinMax()

def test_getSize2D() -> None:
    for i in range(10000):
        nl=randint(1,10)
        nc=randint(1,10)
        mn=randint(-20,-5)
        mx=randint(5,20)
        tab=getRegularArray2D(nl, nc, mn, mx)
        assert isRegular(tab), "Erreur - n'est pas Régulier"
        assert (nl,nc)==getSize2D(tab), "Erreur - n'a pas les mêmes dimensions"
        assert getMin(tab)>=mn and getMin(tab)<=getMax(tab) and getMax(tab)<=mx, "Erreur - n'a pas les tailles respecter"

    print("La fonction getRegularArray2D est correcte !")

test_getSize2D()