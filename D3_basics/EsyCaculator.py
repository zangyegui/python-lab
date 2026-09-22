def easycaculator(a,b,c):
    try:
        match c:
            case '+':
                print(int(a) + int(b))
            case '-':
                print(int(a) - int(b))
            case '*':
                print(int(a) * int(b))
            case '/':
                print(int(a) / int(b))
            case _:
                print("please input correct caculator_note!")
    except ValueError as e:
        print("please input number")
    except ZeroDivisionError as e:
        print("ZeroDivisionError")
a,c,b = input("please input:")
easycaculator(a,b,c)