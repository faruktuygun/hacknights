#!/usr/bin/env python
import os

path = '/'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))


for f in files:
    print f
