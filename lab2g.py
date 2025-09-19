#!/usr/bin/env python3
# Author: Kaiming Chen
# Author ID: kchen129
# Created: 2025/09/18 

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])   
else:
    timer = 3                 

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
