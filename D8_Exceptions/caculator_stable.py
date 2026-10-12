def read_number(prompt:str)->float:
    """"不断询问，直到拿到一个合法整数"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please input a number")

def caculator():
    a = read_number("please input a number as dividend:")
    while(True):
        b = read_number("please input a number(zero illegal) as divisor:")
        try:
            return a / b
        except ZeroDivisionError:
            print("zero can't be a divisor")
        finally:
            pass #test finally uasge         
def main():
    print(caculator())

if __name__ == '__main__':
    main()