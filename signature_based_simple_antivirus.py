#!/usr/bin/env python
import os
import hashlib

path = '/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.elf' in file:
            files.append(os.path.join(r, file))

x="d258a9a1a4055dd1990dff4a27846cda"
for f in files:
    hasher = hashlib.md5()
    with open(f, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    if hasher.hexdigest()==x:
       print f ,",dangerous"
