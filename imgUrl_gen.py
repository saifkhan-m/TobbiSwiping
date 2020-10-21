import os
from itertools import groupby 

basepath = 'men/'
imglst = os.listdir(basepath)
imglst.sort() 
res = [list(i) for j, i in groupby(imglst, 
              lambda a: a.partition('-')[0])] 

with open('imgUrl_gen.csv', 'w') as f:
    f.write(f"Original,Scramble\n" )
    for item in res:
        f.write(f"{basepath+item[0]},{basepath+item[1]}\n" )