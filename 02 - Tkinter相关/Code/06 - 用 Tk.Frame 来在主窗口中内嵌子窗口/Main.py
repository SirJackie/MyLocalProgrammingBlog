from tkinter import *
import win32gui
import win32con
import time
import os

os.system("start python SubWindow.py")
time.sleep(1)


def CreateWindow(width, height, title):
    root = Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


root = CreateWindow(1000, 700, "MainWindow")

frame = Frame(root, width=1000, height=700)
hwnd = win32gui.FindWindow(None, u"SubWindow")  # 获取窗口句柄
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 500, 500, win32con.SWP_SHOWWINDOW)  # 更改窗口在Frame里面的位置


win32gui.SetParent(hwnd, frame.winfo_id())  # 显示窗口
frame.place(x=0, y=0)


def winfun():
    s = win32gui.GetWindowText(hwnd)
    if len(s) > 3:
        print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
    return 1


hwnd = win32gui.FindWindow(None, u"MainWindow")  # 获取窗口句柄
win32gui.EnumChildWindows(hwnd, winfun, None)
# win32gui.SetWindowPos(childHwnd, win32con.HWND_TOPMOST, 0, 0, 500, 500, win32con.SWP_SHOWWINDOW)  # 更改窗口在Frame里面的位置

root.mainloop()
