#encoding:utf-8
#批量修改一个目录下的所有文件名,以数字递增方式重命名

import os  
dir="G://1" #目录名
#filenames=os.listdir(dir)   #读取dir的文件目录 与下面一行代码只启用一个
filenames=os.listdir(os.getcwd())  #读取当前目录 与上面一行代码只启用一个
for filename in range(len(filenames)):  #遍历filenames的文件名长度，并以此为范围.这里如果输出的话是1-50(我目录里有50个文件,不知道为什么是1-50)
    if filenames[filename]!='1.py':     #不修改自身的py文件,如果没这句,自身1.py的文件也会被改名
        os.rename(filenames[filename],str(filename)+'.doc')  #filenames[filename]代表文件名,用rename方法修改文件名


    