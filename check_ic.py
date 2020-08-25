# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:55:20 2020

@author: SS
"""


def main():
    inputs = []
    while True:
        x = input()
        inputs.append(x)
    
    if not inputs or inputs[0] == 0:
        print('N')
    
    inputs = inputs[1:]
    for number in inputs:
        validate(number)

def validate(number):
    if not number:
        print('N')

    string = str(number)
    if len(string) != 11:
        print('N')

    # compute
    result = 0
    for i, digit in enumerate(string):
        digit = int(digit)
        if i == 0 or i == 4 or i == 8 or i == 10:
            result += digit
        elif i == 1 or i == 5 or i == 9:
            result += 3 * digit
        elif i == 2 or i == 6:
            result += 7 * digit
        else:
            result += 9 * digit

    remainder = result % 10
    if remainder == 0:
        print('Y')
    else:
        print('N')
    

if __name__ == '__main__':
    main()