## 01 - Canvas

```
https://baijiahao.baidu.com/s?id=1737407082357297685&wfr=spider&for=pc
```

## 02 - Canvas Update 刷新 & 双缓冲问题

## 03 - 获取屏幕分辨率

```
https://www.codenong.com/3129322/
```

Windows下：

```
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
```

Linux/Mac OS下：

```
import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
```

使用截屏方法获取分辨率：

```
pip install Pillow
```

```
from PIL import ImageGrab

img = ImageGrab.grab()
print (img.size)
```

## 04 - 高DPI支持

```
SetDPIState: 
GetDPIState: https://blog.csdn.net/qq_37887537/article/details/107531596
```



## 05 - Tk.Scaling 规则

## 06 - 用 Tk.Frame 来在主窗口中内嵌子窗口



