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
            return item

        
#test
L = [[1,2],[3,[4,0]],5]

flatten_L = []
gen = flatten(L)
while True:
        try:
            flatten_L.append(next(gen))
        except Exception:
            break
print(flatten_L)
print(flattening_recursion(L))