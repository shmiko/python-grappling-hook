#!/usr/bin/python3
import sys

first_arg = sys.argv

def factorial(first_arg):
    print("factorial has been called with n = " + str(first_arg))
    if first_arg == 1:
        return 1
    else:
        res = first_arg * factorial(first_arg-1)
        print("intermediate result for ", first_arg, " * factorial(" ,first_arg-1, "): ",res)
        return res

print(factorial(first_arg))
# factorial()
