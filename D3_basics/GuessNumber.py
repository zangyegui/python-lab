import random
i = random.randint(1,100)
n = None
while((i != n)):
    try:
        n = (input("please guess the int number:"))
        if int(n) > i :
            print("the guessed number is large")
        elif int(n) < i:
            print("the guessed number is small")
        else:
            print("Guess correct!")
    except Exception as e:
        print("Please input int number")

