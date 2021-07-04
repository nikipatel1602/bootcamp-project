# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:47:01 2021

@author: patel niki k
"""

import hashlib

result = hashlib.md5(b'hello shapeai')

print("the byte equivalent of hash is:",end="")
print(result.digest)