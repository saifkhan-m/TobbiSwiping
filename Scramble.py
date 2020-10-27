import os
from PIL import Image
import random
from datetime import datetime

def scramble(key,fileName,basepath):
    image = Image.open(basepath+fileName)
    pixels = image.load()
    new_image = Image.new(image.mode,image.size)
    new_image_pix = new_image.load()
    seed = 0
    for c in key:
        seed+=ord(c)
    random.seed(seed)
    for i in range(0,(image.size)[0]):
        for j in range(0,(image.size)[1]):
            new_image_pix[i,j] = pixels[random.randint(0,image.size[0]-1),
                                        random.randint(0,image.size[1]-1)]
    fileNamelst=fileName.split('.')
    new_image.save(basepath+fileNamelst[0].replace('original', 'scramble')+'.'+fileNamelst[1])

#basepath = 'women1/'
basepath = 'men1/'
for img in os.listdir(basepath):
    scramble('abc',img,basepath)