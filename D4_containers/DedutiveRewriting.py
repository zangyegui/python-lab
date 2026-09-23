#需要改写的片段
# result = []
# for x in [1,2,3,4,5,6]:
#     if x % 2 == 0:
#         result.append(x)
result = [x for x in range(1,7) if x % 2 == 0]
print(result)

result1 = [x ** 2 for x in range(1,7) ]
print(result1)

ls = [("Adam",99),("Bob",60),("Cur",63),("David",75),("Eliver",79),("Fuzz",80),("Grad",89),("Hery",94),("I",64)]
result2 = [x[0] for x in ls if x[1] >= 90]
print(result2)