def flatening(L):
    l = []
    for i in L:
        if isinstance(i,list):
            for j in i:
                l.append(j)
        else:
            l.append(i)
    return l

#test
L = [[1,2],[3,4],5]
print(flatening(L))