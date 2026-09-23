def FindMinAndMax(L):
    if not L:
        return(None,None)
    else:
        for i in L:
            if i == L[0]:
                max = i
                min = i
            else:
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
elif (FindMinAndMax([7,1,3,9,5])!=(1,9)):
    print("test failed!")
else:
    print("test succeed!")