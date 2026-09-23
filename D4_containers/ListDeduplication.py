ls = [3,1,2,3,1,5,2]
s = []
s1 = list(dict.fromkeys(ls))
for value in ls:
    if value not in s:
        s.append(value)
print(s)
print(s1)
