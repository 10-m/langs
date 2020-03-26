#!env python3
# -*- coding: utf-8 -*-
import logging
import os

# コンソールに表示するのは INFO レベル以上。
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(
    '%(pathname)s:%(lineno)s:%(funcName)s %(message)s'
))

# ファイルに出力するのは ERROR レベル以上。
file_handler = logging.FileHandler('./tmp.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(
    ' '.join(['%(asctime)s',
             '[%(levelname)s]',
             '%(pathname)s:%(lineno)s:%(funcName)s',
             '%(name)s',
             '%(message)s'])))

logging.basicConfig(
    level=logging.INFO,
    handlers=[stream_handler, file_handler]
)

logger = logging.getLogger(__name__)

def test_func():
    logger.info("start main")
    logger.error("something error")
    logger.info("end main")

if __name__ == '__main__':
    test_func()
    logger.info("in script")
    logger.error("in script")
    with open('./tmp.log', 'r') as f:
        print(f.read(), end='')
    os.remove('./tmp.log')

