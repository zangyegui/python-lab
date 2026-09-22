import random
i = random.randint(1,100)
n = None
count = 0
while((i != n)):
    try:
        n = (input("please guess the int number:"))
        if int(n) > i :
            print("the guessed number is large")
        elif int(n) < i:
            print("the guessed number is small")
        else:
            print("Guess correct!")
        count = count + 1
    except Exception as e:
        print("Please input int number")
print(f"Guess count is{count}")

