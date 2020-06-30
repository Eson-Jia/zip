#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

the_reg = re.compile('(.{2,4}?)版?([789七八九])([上下]).+?(\d{1,2})')

m = the_reg.match(content)
print(m[1])
print(m[2])
print(m[3])
print(m[4])
