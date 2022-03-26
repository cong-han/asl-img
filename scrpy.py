"""
功能: 将某文件夹下的图片批量转化为jpg, 并移动到'converted'文件夹下
步骤:
1. 遍历文件夹内的文件
2. 获取原文件名infile(带路径和后缀)
3. 判断文件格式 != jpg
    3.1 true: 转化为 outfile
    3.2 将infile移动到"convert"文件夹
遇到的问题:
转jpg报错, 需要加convert("RGB")
https://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
"""

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
    if ex != ".jpg":  #"_"代表已经转过了
        try:
            Image.open(infile).convert("RGB").save(outfile)
            movefile = "converted/" + "d_" + pic
            shutil.move(infile, movefile)
            print("SUCCESS")
        except OSError:
            print("cannot convert", infile)
print("finished")
