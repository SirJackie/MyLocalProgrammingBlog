## 01 - Canvas

```
https://baijiahao.baidu.com/s?id=1737407082357297685&wfr=spider&for=pc
```

```python
# Draw Geometries
canvas.create_line(x1, y1, x2, y2, fill="black")
canvas.create_oval(x, y, width, height, fill="white", outline="black")
canvas.create_rectangle(x, y, width, height, fill="white", outline="black")

# Draw Image
# Support gif, some versions of tkinter support png, no jpg support
imageObj = PhotoImage(file="Image.png")
canvas.create_image(0, 0, image=imageObj, anchor=tk.NW)

# Draw Font
# Tk Colors: 1.String:red,white,green,blue,yellow; 2.HexColor:#FFFF00
canvas.create_text(
    (20, 50),
    text="你好，世界！Hello World!",
    font=("黑体", 30),
    fill="#FFFF00",
    anchor=tk.W,
    justify=tk.LEFT
)
```

## 02 - Canvas Update 刷新 & 双缓冲问题

## 03 - 获取屏幕分辨率

```
GetResolution: https://www.codenong.com/3129322/
SetDPIState: https://blog.csdn.net/qq_25921925/article/details/103987572
GetDPIState: https://blog.csdn.net/qq_37887537/article/details/107531596
```

Windows/Linux/Mac OS通用方法（Tkinter API）：

```python
import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
```

Windows下（Win32 API）：

```python
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
```

**要注意，Windows下，不管用Win32 API还是Tkinter API，都无法获取真实分辨率。**

想获取真实分辨率，需要明白Windows下的窗口有两种模式：

> Windows' Window has 2 modes:
>
> 1. Low DPI Mode (Compatibility Mode)
> 2. High DPI Mode (Modern Mode)
>
> When in mode 1, GetScreenLowDPIResolution() will return fake resolution 
>
> (compatible resolution)
>
> We need to first sf = GetScalingFactor(), then do GetScreenLowDPIResolution() * sf
>
> When in mode 2, GetScreenLowDPIResolution() will return true resolution
>
> Moreover, we need to judge which mode we are inside (using IsHighDPIModeOpened())

所以：正确的获取Windows下真实分辨率的方法：

```python
import ctypes
import os
import tkinter as tk


osType = None

if os.name == "nt":
    osType = "Windows"
elif os.name == "posix":
    osType = "Linux"
else:
    osType = "Others"


def GetScalingFactor():
    if osType == "Windows":
        scalingFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        return scalingFactor / 100
    else:
        # Linux has no compatibility mode, High DPI is always enabled, so no need to scale
        return 100 / 100


def EnableHighDPIMode():
    if osType == "Windows":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    else:
        # Linux has no compatibility mode, High DPI is always enabled
        pass


def IsHighDPIModeOpened():
    if osType == "Windows":
        awareness = ctypes.c_int()
        errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        if awareness.value == 0:
            return False
        else:
            return True
    else:
        # Linux has no compatibility mode, High DPI is always enabled
        return True


def GetScreenResolutionUsingTkinterDPI():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height


def GetScreenLowDPIResolution():
    if osType == "Windows":
        # Use Win32 API to get resolution
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    else:
        # Use Tkinter API to get resolution
        return GetScreenResolutionUsingTkinterDPI()


def GetScreenResolution():
    if osType == "Windows":

        # Windows' Window has 2 modes:
        # 1. Low DPI Mode (Compatibility Mode)
        # 2. High DPI Mode (Modern Mode)
        # When in mode 1, GetScreenLowDPIResolution() will return fake resolution (compatible resolution)
        #     We need to first sf = GetScalingFactor(), then do GetScreenLowDPIResolution() * sf
        # When in mode 2, GetScreenLowDPIResolution() will return true resolution
        # Moreover, we need to judge which mode we are inside (using IsHighDPIModeOpened())

        mode = IsHighDPIModeOpened()
        if mode is True:
            # Inside: 2. High DPI Mode (Modern Mode)
            return GetScreenLowDPIResolution()

        elif mode is False:
            # Inside: 1. Low DPI Mode (Compatibility Mode)
            sf = GetScalingFactor()
            w, h = GetScreenLowDPIResolution()
            w *= sf
            h *= sf
            w = int(w)
            h = int(h)
            return w, h

    else:
        # Linux has no compatibility mode, High DPI is always enabled
        # No mode judging issue, so just return GetScreenLowDPIResolution()
        return GetScreenLowDPIResolution()
```

附加：旁门左道：使用截屏方法获取分辨率：

```shell
pip install Pillow
```

```python
from PIL import ImageGrab

img = ImageGrab.grab()
print (img.size)
```

## 04 - Tk.Scaling 规则

```
TkScaling: https://blog.csdn.net/fzipw/article/details/127942079
```

启用TkScaling方法：

```
root.tk.call('tk', 'scaling', 1.33333)
```

其中，1.33333是缩放倍数。如果不设置的话，默认就是1.33333（就是100÷75）而不是1，这是个大坑。

1.33333是因为：

> 链接: https://www.tcl.tk/man/tcl8.6/TkCmd/tk.html.
> tkinter有一个内部缩放因子,用于将点和英寸等测量值转换为像素.您可以使用"tk scaling"命令进行设置.此命令采用一个参数,即一个"点"中的像素数.一个点是1/72英寸,因此缩放因子1.0适用于72DPI显示器.
> 通常在缩放比率在100%时这个比率为 96/72=1.3333…
> 你也可以使用 self.tk.call(‘tk’, ‘scaling’) 查看当前值

## 05 - 高DPI支持

```
WinDPI: https://blog.csdn.net/qq_25921925/article/details/103987572
TkScaling: https://blog.csdn.net/fzipw/article/details/127942079
```

Tkinter的高DPI支持，有两种方法：

- 在创建root窗口对象**之间**，打开Windows高DPI模式
  - 优点：更容易实现，自动支持缩放，不需要手动TkScaling
  - 缺点：自动缩放和Windows显示设置里面的“缩放比例”（100%、125%）正相关，与系统耦合
- 在创建root窗口对象**之后**，打开Windows高DPI模式：
  - 优点：可以自定义缩放比例
  - 缺点：更麻烦，一开始会所有的控件都变小，需要自己使用TkScaling手动缩放来修正

我一般使用第二种方法，来获得更大的可控制性和Linux兼容性。

需要注意的是，TkScaling只对相对布局、控件的字体大小有影响，对绝对布局、Canvas大小、窗口则没有影响。这是很好的特性，这样就不会因为TkScaling到200%，窗口大小就要除以2。

打开Windows高DPI模式的方法见`03 - 获取屏幕分辨率`。

使用TkScaling方法见`04 - Tk.Scaling 规则`。

## 06 - 用 Tk.Frame 来在主窗口中内嵌子窗口

```
https://blog.csdn.net/tinga_kilin/article/details/108291802?spm=1001.2014.3001.5502
```



## 07 - Tkinter布局助手：拖拽式布局Tkinter

在线使用

https://www.pytk.net/tkinter-helper/

github仓库

https://github.com/iamxcd/tkinter-helper

知乎专栏1

https://zhuanlan.zhihu.com/p/530986081?utm_id=0

知乎专栏2

https://zhuanlan.zhihu.com/p/532678277

## 08 - Matplotlib内嵌到Tkinter

内存溢出：matplotlib与tkinter的简单使用，以及内存溢出问题。

https://blog.csdn.net/qq_44817900/article/details/124302515

官网教材：tkinter内嵌Matplotlib系列（一）之解读官网教材

https://www.cnblogs.com/zyg123/p/10385456.html

PyPlot vs. 面向对象画图：tkinter+ pyplot API无法退出进程

https://blog.csdn.net/charie411/article/details/107365526/

## 09 - Webview内嵌到Tkinter

tkinter使用WebView2网页组件

https://blog.csdn.net/tinga_kilin/article/details/122141490

## 10 - Vvvebjs：拖拽式搭建Web界面，可结合Tkinter

中文介绍：VvvebJs–使用开源的JavaScript网站可视化构建库拖拽生成网页

http://www.yixao.com/procedure/9700.html

介绍：拖拽生成web网页_网页设计，使用拖拽的方式生成网页！JavaScript库——VvvebJs

https://blog.csdn.net/weixin_39861624/article/details/113370622

开源中国的介绍

https://www.oschina.net/p/vvvebjs?hmsr=aladdin1e1

在线使用

http://www.vvveb.com/vvvebjs/editor.html

gitee仓库

https://gitee.com/mirrors/VvvebJs