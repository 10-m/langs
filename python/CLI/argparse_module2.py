#!env python3
# -*- coding: utf-8 -*-
import argparse

# python3 argparse_module2.py 1 2
# python3 argparse_module2.py 1 2 3

def mul(a, b, c):
    return a * b * c

if __name__ == "__main__":
    parser = argparse.ArgumentParser("multiply three values")
    parser.add_argument("numbers", help="float values", 
                        type=float, nargs=3) 
    args = parser.parse_args()
    print(mul(args.numbers[0], args.numbers[1], args. numbers[2]))
