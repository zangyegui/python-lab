def flattening_recursion(L):
    result = []
    for i in L:
        if isinstance(i,list):
           result.extend(flattening_recursion(i))
        else:
            result.append(i)
    return result

def flatten(L):
    for item in L:
        if isinstance(item,list):
            yield from flatten(item)
        else:
            yield item

        
#test
L = [[1,2],[3,[4,0]],5]

flatten_L = []
print(list(flatten(L)))
print(flattening_recursion(L))