#!env python3
# -*- coding: utf-8 -*-
import os
import tempfile
import unittest

class TestUsingTempFile(unittest.TestCase):
    def test_using_temp_file(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write('\n'.join(['aaa', 'bbb', 'ccc']) + '\n')
            f.flush()
            with open(f.name, 'r') as fd:
                actual = len(fd.readlines())
        self.assertEqual(actual, 3)

    def test_using_temp_dir(self):
        with tempfile.TemporaryDirectory() as dirpath:
            with open(os.path.join(dirpath, 'file1'), mode='w', encoding='utf-8') as f1, \
                 open(os.path.join(dirpath, 'file2'), mode='w', encoding='utf-8') as f2:
                actual = len(os.listdir(dirpath))
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main()
