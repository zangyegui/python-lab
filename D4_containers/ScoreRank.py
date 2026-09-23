ls = [("Adam",59),("Bob",60),("Cur",63),("David",75),("Eliver",79),("Fuzz",80),("Grad",89),("Hery",94),("I",98)]
ls.sort(reverse = True)
for person,score in enumerate(ls):
    print(person+1,score[0])