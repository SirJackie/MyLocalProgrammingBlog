from tkinter import *
import win32gui
from time import sleep as slp


def CreateWindow(width, height, title):
    root = Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


root = CreateWindow(1000, 500, "ChessUI")

resultFrame = Frame(root, width=1000, height=500)
hid = win32gui.FindWindow(None, u"SubWindow")  # 获取窗口句柄
win32gui.SetParent(hid, resultFrame.winfo_id())  # 显示窗口
resultFrame.place(x=0, y=0)

root.mainloop()
