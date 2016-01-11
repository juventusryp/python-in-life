#读取一个目录下所有文件名，按照文件名中的空格输出为txt
import os
import os.path
rootdir = os.getcwd() #获取当前文件夹路径
with open('tt.txt','w') as f:
    for parent,dirnames,filenames in os.walk(rootdir):  #获取文件名，目录名
        for filename in filenames:
            a = filename.split()
            str1 = " ".join(str(i) for i in a)
            print(str1)
            f.write(str1)
            f.write('\n')


