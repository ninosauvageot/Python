def indexOf(lst,val):
    res=-1
    for i in range(len(lst)):
        if lst[i]==val and res==-1:
            res=i
    return res

def indexOfSorted(lst,val)->tuple:
    res = -1
    compteur=0
    for i in range(len(lst)):
        if lst[i]<=val:
            if lst[i] == val and res == -1:
                res = i
            elif res==-1:
                compteur += 1

    return res,compteur

def binarySearch(lst,val):
    ideb=0
    ifin=len(lst)
    res=-1
    imilieu = (ifin+ideb) // 2
    while res == -1 and ideb!=ifin:
        if lst[imilieu]<val:
            ideb=imilieu+1
            imilieu = ((ifin+ideb) // 2)
        elif lst[imilieu]>val:
            ifin=imilieu
            imilieu = (ifin+ideb) // 2
        else:
            res=imilieu
    return res

def getReponse(val):
    print("Proposition de l'ordinateur : " ,val)
    user=input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : ").upper()
    rep=["E","G","P"]
    while user not in rep:
        print(f"Réponse {user} incorrecte, tapez E, G ou P.")
        print("Proposition de l'ordinateur : " ,val)
        user= input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : ").upper()

    return user


def devinerNombre(mn: int, mx: int) -> None:
    print(f"Choisissez un nombre entre {mn} et {mx}...")
    choice = (mn + mx) // 2
    res = getReponse(choice)
    compt = 1
    while res != "E" and mn < mx:
        if res == "P":
            mx = choice - 1
        elif res == "G":
            mn = choice + 1
        choice = (mn + mx) // 2
        res = getReponse(choice)
        compt += 1
    if res == "E":
        print(f"Nombre deviné en {compt} coups.")
    else:
        print("Je n'ai pas trouvé !?")


