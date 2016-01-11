import os
import os.path
rootdir = os.getcwd()
with open('tt.txt','w') as f:
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            a = filename.split()
            str1 = " ".join(str(i) for i in a)
            print(str1)
            f.write(str1)
            f.write('\n')


