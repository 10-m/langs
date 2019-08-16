#!env python3
# -*- coding: utf-8 -*-
import argparse

# python3 argparse_module.py
# python3 argparse_module.py -h
# python3 argparse_module.py -a 1 -b 2 -c 3

def mul(a, b, c):
    return a * b * c

if __name__ == "__main__":
    parser = argparse.ArgumentParser("multiply three values")
    parser.add_argument("-a", help="value1", type=float, 
                        required=True)
    parser.add_argument("-b", help="value2", type=float, 
                        required=True)
    parser.add_argument("-c", help="value3", type=float, 
                        default=1)
    args = parser.parse_args()
    print(mul(args.a, args.b, args.c))
