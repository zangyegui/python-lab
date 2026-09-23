ls = [("Adam",99),("Bob",60),("Cur",63),("David",75),("Eliver",79),("Fuzz",80),("Grad",89),("Hery",94),("I",64)]
ls.sort(key = lambda x:x[1] ,reverse = True)
for person,score in enumerate(ls):
    print(f"{person+1} {score[0]} {score[1]}")