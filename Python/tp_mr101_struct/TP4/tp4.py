from random import *


def getRegularArray2D(nl, nc, mn, mx):
    alea = randint(mn, mx)
    lst = []
    tmp = []
    for i in range(nl):
        tmp = []
        for j in range(nc):
            tmp.append(alea)
            alea = randint(mn, mx)
        lst.append(tmp)
    return lst


def isRegular(lst):
    res = True
    for i in range(len(lst) - 1):
        if len(lst[i]) == len(lst[i + 1]) and res == True:
            res = True
        else:
            res = False
    return res


def getMin(lst):
    res = lst[0][0]
    i = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] < res:
                res = lst[i][j]
    return res

def getMax(lst):
    res = lst[0][0]
    i = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] > res:
                res = lst[i][j]
    return res

def getSize2D(lst):
    nbligne=0
    nbcolone=0
    for i in range(len(lst)):
        nbligne+=1
        nbcolone = 0
        for j in range(len(lst[i])):
            nbcolone+=1
    res=(nbligne,nbcolone)
    return res















