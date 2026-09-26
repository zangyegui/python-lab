def FindMinAndMax(L):
    if not L:
        return(None,None)
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
    return(min,max)

#test
if(FindMinAndMax([])!=(None,None)):
    print("test failed!")
elif (FindMinAndMax([7])!=(7,7)):
    print("test failed!")
elif (FindMinAndMax([7,1])!=(1,7)):
    print("test failed!")
elif (FindMinAndMax([7,1,7])!=(1,7)):
    print("test failed!")
elif (FindMinAndMax([7,1,3,9,5])!=(1,9)):
    print("test failed!")
else:
    print("test succeed!")