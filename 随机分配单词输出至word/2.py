import random
import win32com
from win32com.client import Dispatch, constants
import itertools
import random

w = win32com.client.Dispatch('Word.Application')
#后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0
doc = w.Documents.Add()

myRange = doc.Range(0,0)
myRange.Style.Font.Name = "宋体"
myRange.Style.Font.Size = "16"

words = range(1,250)


myRange.InsertAfter('第一组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))  #随机从words中选取18个单词插入到文件
myRange.InsertAfter('\n')

myRange.InsertAfter('第二组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第三组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第四组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第五组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第六组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第七组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第八组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第九组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十一组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十二组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十三组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十四组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('\n')
myRange.InsertAfter('第十五组:')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十六组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十七组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

myRange.InsertAfter('第十八组:')
myRange.InsertAfter('\n')
myRange.InsertAfter(random.sample(words, 18))
myRange.InsertAfter('\n')

doc.SaveAs(r'D:\d.doc')

doc.Close()
w.Quit()


