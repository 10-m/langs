#!env python3
# -*- coding: utf-8 -*-
import argparse
from pprint import pprint

if __name__ == "__main__":
     
    # パーサーを作る
    parser = argparse.ArgumentParser(
                prog='argparseTest.py', # プログラム名
                usage='Demonstration of argparser', # プログラムの利用方法
                description='description', # 引数のヘルプの前に表示
                epilog='end', # 引数のヘルプの後で表示
                add_help=True, # -h/?help オプションの追加
                )
     
    # 引数の追加
    parser.add_argument('-v', '--verbose',
                        help='select mode',
                        action='store_true',
                        required=True)
    parser.add_argument('-int',
                        help='interger',
                        type=int,
                        default=1)
    parser.add_argument('s',
                        help='string',
                        type=str,
                        choices=['a', 'b'])

    parser.add_argument('mul', help='multiply',
                        type=float,
                        nargs=2,
                        metavar='hoge') # ヘルプやエラーの出力時の引数名を設定
    parser.add_argument('-i', help='inputfile',
                        type=argparse.FileType('r'))
    parser.add_argument('-o', help='outputfile',
                        type=argparse.FileType('w'))

    # 引数を解析する
    args = parser.parse_args()
    pprint(vars(args))

# python3 ./argparse_module.py -h
# python3 ./argparse_module.py -v a 1 2 -i ./argparse_module.py ./dummy.py
