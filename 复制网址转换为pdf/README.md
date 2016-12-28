### 作用

浏览器复制url，通过autohotkey转换为pdf

### 效果
![1.gif](http://upload-images.jianshu.io/upload_images/1061851-ad92a5e28fb90c99.gif?imageMogr2/auto-orient/strip)

### 依赖

1、wkhtmltopdf  
下载地址：[http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html)  
把wkhtmltopdf目录下的bin目录添加到系统路径path中

2、安装pdfkit  pyperclip  
pip install pdfkit  
pip install pyperclip  

3、autohotkey  
下载地址：[http://www.ahkscript.org/](http://www.ahkscript.org/)

### 使用方法

1、将下载的三个文件放到桌面（如果你想放到其他目录，需要自行修改里面的路径代码）

2、打开htmltopdf.ahk

3、浏览器复制想要转换的url

4、windows键+空格

5、大功告成，在桌面就会生成pdf文件


### Update:
2016-12-28 增加按照当前电脑时间日期保存pdf


