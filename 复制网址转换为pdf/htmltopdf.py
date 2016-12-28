import pdfkit
import pyperclip
import time

a=str(pyperclip.paste())
filename = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))+'.pdf'
pdfkit.from_url(a, '%s' % filename)