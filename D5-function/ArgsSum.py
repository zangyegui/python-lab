def sum_all(*args):
    total = 0
    for i in args:
        if not isinstance(i,(int,float)):
            raise TypeError(f"sum_all只接收数字,收到了{i}!")
        else:
            total += i
    return total

print(sum_all(1,2,3,4))
print(sum_all())
print((sum_all(True,1)))
print(sum_all(1,'a',2,'b'))