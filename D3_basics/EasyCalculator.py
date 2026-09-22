def easycalculator(x,y,op):
    try:
        match op:
            case '+':
                print(int(x) + int(y))
            case '-':
                print(int(x) - int(y))
            case '*':
                print(int(x) * int(y))
            case '/':
                print(int(x) / int(y))
            case _:
                print("please input correct calculator_note!")
    except ValueError:
        print("please input numxer")
    except ZeroDivisionError:
        print("ZeroDivisionError")
a,c,b = input("please input:").split()

easycalculator(a,b,c)