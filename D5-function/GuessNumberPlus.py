import random

def Guessnumber(low: int = 1,high: int = 100)->int:
    if not isinstance(low,int) and not isinstance(high,int):
        raise TypeError(f"arg must be int")
    count = 1
    target = random.randint(low,high)
    try:
        n = (input("please guess the number:"))
        while(int(n) != target):
            count += 1
            if int(n) < target:
                print("Guess smaller")
                n = (input("Guess again:"))
            elif int(n) > target:
                print("Guess laeger")
                n = (input("Guess again:"))
        print(f"Guess correct,and you tried {count} counts")
    except TypeError:
        print(f"please input int")

Guessnumber()
Guessnumber(1,10)
Guessnumber('a',6)