# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = int(input("Enter X: "))
x += 1
for i in range(1,x):
    print(" "*(x-i-1), end="")
    print("*"*(2*i-1))