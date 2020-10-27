import os
from itertools import groupby 

basepath = 'women1/'
#basepath = 'men1/'
imglst = os.listdir(basepath)
counter = 1
for i in sorted(imglst):
    if 'scramble' not in i:
        os.rename(basepath+i, basepath+str(counter)+'-original'+'.jpg')
        counter+=1