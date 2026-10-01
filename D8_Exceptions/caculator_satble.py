def read_int(prompt:str)->float:
    """"不断询问，直到拿到一个合法整数"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please input int number")

def caculator():
    a = read_int("please input a number as dividend:")
    b = read_int("please input a number(zero illegal) as divisor:")
    try:
        return a / b
    except ZeroDivisionError:
        print("zero can't be a divisor")
    finally:
        pass

def main():
    print(caculator())

if __name__ == '__main__':
    main()