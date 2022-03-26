import os
import shutil
from PIL import Image

# Image.open("awl-img/15388034124_f6d1b630af_k.jpg").show()

#shutil.move("awl-img/_1.txt", "converted/_2.txt")
#os.rename(dir + "2.txt", dir + "_" + "1.txt")

dir = "awl-img/"
for pic in os.listdir(dir):
    infile = dir + pic
    name, ex = os.path.splitext(pic)
    outfile = dir + name + ".jpg"
    if ex != ".jpg" and pic[0] != "_":  #"_"代表已经转过了
        try:
            Image.open(infile).convert("RGB").save(outfile)
            movefile = "converted/" + pic
            shutil.move(infile, movefile)
            #os.rename(infile, dir + "_" + pic)
            print("SUCCESS")
        except OSError:
            print("cannot convert", infile)
print("finished")
"""
遇到的问题:
转jpg报错, 需要加convert("RGB")
https://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
"""