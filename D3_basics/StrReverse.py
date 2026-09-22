s = "Hello World"
s2 = s[::-1]
print(s2)
ls = s.split()
s3 = ls[0][::-1]
s4 = ls[1][::-1]
s5 = " ".join([s3,s4])
print(s5)