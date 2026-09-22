s = input("please input a string:")
s2 = s[::-1]
print(s2)
ls = s.split()
s3 = " ".join(w[::-1] for w in ls)
print(s3)