import random

def read_int(prompt:str)->int:
    """"不断询问，直到拿到一个合法整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("please input int number")
    
def Guessnumber(low: int = 1,high: int = 100)->int:
    if not isinstance(low,int) or not isinstance(high,int):
        raise TypeError(f"arg must be int")
    count = 0
    target = random.randint(low,high)
    while True:
        n = read_int("please input guess number:")
        count += 1
        if n < target:
            print("Guess larger")
        elif n > target:
            print("Guess smaller")
        else:
            return count

if __name__ =='__main__':
    # print(f"Guess correct ,you tried {Guessnumber()}")
    results = [Guessnumber(1,10) for _ in range(2)]
    print(f"success twice,you tried {results}")
    print(f"Guess correct ,you tried {Guessnumber('a',6)}")