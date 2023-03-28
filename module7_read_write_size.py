#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      СТВН
#
# Created:     22.03.2023
# Copyright:   (c) СТВН 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
a = os.listdir()
b = os.getcwd()
stats = os.stat(b)
print (b)
with open("listdir.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())


with open("listdir.txt", "a") as f:
    f.write(b+'\n')
    for i in a:
        size = os.path.getsize(i)
        f.write(i+' - размер в байтах: '+str(size)+'\n')
