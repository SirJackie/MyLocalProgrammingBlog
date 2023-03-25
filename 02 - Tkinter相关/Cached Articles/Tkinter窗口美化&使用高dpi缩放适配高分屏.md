# Tkinter窗口美化&使用高dpi缩放适配高分屏

```
https://blog.csdn.net/qq_25921925/article/details/103987572
```

## 1.让Tkinter小部件具有Windows本地风格

```python
from tkinter import *
from tkinter.ttk import *
```

## 2.解决高分屏下程序界面模糊问题（高DPI适配）

```python
import ctypes
#告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#获取屏幕的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
#设置程序缩放
root.tk.call('tk', 'scaling', ScaleFactor/75)
```

## 3.方法总结

```python
#导入库
import ctypes
from tkinter import *
from tkinter.ttk import *

#创建窗口，root可替换成自己定义的窗口
root=Tk()
#调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#调用api获得当前的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
#设置缩放因子
root.tk.call('tk', 'scaling', ScaleFactor/75)
```

## 4.附上演示程序的全部代码

```python
import ctypes
from tkinter import *
from tkinter.ttk import *
def fac(x):
    if x==0 or x==1:
        return 1
    elif x>1:
        return x*fac(x-1)
root=Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
root.title('计算阶乘')
frame1=Frame(root)
frame1.pack(side='top',anchor='center',expand='yes')
lable1=Label(frame1,text='input')
lable2=Label(frame1,text='output')
entry1=Entry(frame1)
entry2=Entry(frame1)
def button1_clicked():
    entry2.delete(0,END)
    entry2.insert(0,str(fac(eval(entry1.get()))))
button1=Button(frame1,text='Run',command=button1_clicked)
button2=Button(frame1,text='Quit',command=root.quit)
lable1.grid(row=0,column=0,pady=3,padx=3)
lable2.grid(row=1,column=0,pady=3,padx=3)
entry1.grid(row=0,column=1,pady=3,padx=3)
entry2.grid(row=1,column=1,pady=3,padx=3)
button1.grid(row=2,column=0,sticky=W,pady=3,padx=3)
button2.grid(row=2,column=1,sticky=E,pady=3,padx=3)
root.mainloop()
```

