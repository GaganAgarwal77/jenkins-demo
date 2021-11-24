#!/usr/bin/python3
# Program for calculating factorial of a number

def factorial(n):  
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
