#!/usr/bin/env python3
import re
import os
import sys

if (len(sys.argv) != 2):
    exit("Invalid number of arguments.")

stream = os.popen('javap -c ' + sys.argv[1] + ' | grep invokevirtual')
output = stream.read()
classNames = set(re.findall(r'(?<=Method )[^.:]*?(?=\..*?:)|(?<=[;|\(|\)]L)[^\(\);]*?(?=;)', output))
for name in classNames:
    print(name)
