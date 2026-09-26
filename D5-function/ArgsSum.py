def sum_all(*args):
    sum = 0
    for i in args:
        if isinstance(i,(int,float)):
            sum = sum + i
        else:
            print("sum_all only support numbers!")
    return sum

print(sum_all(1,2,3,4))
print(sum_all())
print(sum_all(1,'a',2,'b'))