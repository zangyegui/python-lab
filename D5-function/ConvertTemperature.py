#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'欧式/华氏温度互转'

def convert(value,str = "C"):
    try:
        if str == "C":
            return value *9/5 +32
        elif str == "F":
            return (value -32) *5/9
    except TypeError as e:
        print("please input float temperature!")
        return e

if __name__ == '__main__':
    print(convert(37))
    print(convert(37,'C'))
    print(convert(120,'F'))
    print(convert('abc','C'))

