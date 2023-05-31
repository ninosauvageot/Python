def estTrie(lst:list)->bool:
    res = True
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            res=False
    return res

def echanger(lst:list,i1:int,i2:int)->None:

    lst[i1],lst[i2]=lst[i2],lst[i1]

def triBulles(lst:list)->None:
    if estTrie(lst)!=True:
        while estTrie(lst)!=True:
            for i in range(len(lst)-1):
                if lst[i]>lst[i+1]:
                    echanger(lst,i,i+1)

def getMin(lst:list)->int:
    mini=lst[0]
    for i in range(len(lst)):
        if lst[i]<mini:
            mini=lst[i]
    return mini

def getIndexMin(lst:list)->int:
    mini = lst[0]
    res = 0
    for i in range(len(lst)):
        if lst[i] < mini:
            mini = lst[i]
            res = i
    return res

def getIndexMinFrom(lst,dpt):
    mini = lst[dpt]
    res = dpt
    for i in range(dpt,len(lst),1):
        if lst[i] < mini:
            mini = lst[i]
            res = i
    return res


def triSelection(lst):
    for i in range(len(lst)):
        mini = i
        for j in range(i + 1, len(lst)):
            if lst[mini] > lst[j]:
                mini = j
        tmp = lst[i]
        lst[i] = lst[mini]
        lst[mini] = tmp

def deplacerCase(lst,i):

    for j in range(i+1):
        if lst[j]>lst[i]:
            lst.insert(j,lst.pop(i))

def deplacerCaseDys(lst,i):
    tmp=lst[i]
    for j in range(i,0,-1):
        lst[j]=lst[j-1]
        if tmp>=lst[j]:
            lst[j]=tmp
            print(lst)
            return None
    lst[0]=tmp
    print(lst)


def triInsertion(lst):
    while estTrie(lst) == False:
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                deplacerCase(lst, j+1)
    print(lst)

