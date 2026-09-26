#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'摄氏/华氏温度互转'

def convert(value:float,unit:str = "C")->float:
    """摄氏/华氏温度互转：unit='C' 输入摄氏，unit='F' 输入华氏"""
    if not isinstance(value,(int,float)):
        print("please input int/float value!")
        return
    if unit == "C":
        return value *9/5 +32
    elif unit == "F":
        return (value -32) *5/9
   

if __name__ == '__main__':
    print(convert(37))
    print(convert(37,'C'))
    print(convert(120,'F'))
    print(convert('abc','C'))

