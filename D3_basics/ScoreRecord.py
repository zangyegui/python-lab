ls = [("Adam",59),("Bob",60),("Cur",63),("David",75),("Eliver",79),("Fuzz",80),("Grad",89),("Hery",94),("I",98)]
ls.sort(key = lambda x: x[1], reverse = True)
avg_score = sum(x[1] for x in ls) / len(ls)
best_score = max(ls,key = lambda x: x[1])
min_score = min(ls,key = lambda x: x[1])
fail_count = sum(1 for x in ls if x[1] <= 60)

print(f"avrge_score = {avg_score}")
print(f"{best_score[0]} got the best_score = {best_score[1]}")
print(f"min_score = {min_score[1]}")
print(f"the count of fail is {fail_count}")