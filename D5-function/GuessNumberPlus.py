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
                n = (input())
            elif int(n) > target:
                print("Guess laeger")
                n = (input())
        return count
    except TypeError:
        print(f"please input int")

if __name__ =='__main__':
    print(f"Guess correct ,you tried {Guessnumber()}")
    print(f"Guess correct ,you tried {Guessnumber(1,10)}")
    print(f"Guess correct ,you tried {Guessnumber('a',6)}")