import import_example
print(import_example.syaku_to_cm(10))

abbrev_func = import_example.syaku_to_cm
print(abbrev_func(20))

from import_example import syaku_to_cm
print(syaku_to_cm(30))

import import_example as sya
print(sya.syaku_to_cm(40))

from import_example import syaku_to_cm as s2cm
print(s2cm(50))

import mod.import_example2
print(mod.import_example2.syaku_to_cm(60))
