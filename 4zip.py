#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import zipfile

nameMap = {}


tt = re.compile('[789七八九]')


def findSignature(name: str):
    the_reg = re.compile('(.{2,4}?)版?([789七八九])([上下]).+?(\d{1,2})')
    m = the_reg.match(name)
    return (m[0], m[1], m[2], m[3])


# for file in os.listdir('./'):
#     if file in __file__:
#         continue
#     name, ext = os.path.splitext(file)
#     if name not in nameMap:
#         nameMap[name] = []
#     nameMap[name].append(file)
# for name, files in nameMap.items():
#     z = zipfile.ZipFile(name+'.zip', 'w', zipfile.ZIP_DEFLATED)
#     for file in files:
#         z.write(file)
#     z.close()
