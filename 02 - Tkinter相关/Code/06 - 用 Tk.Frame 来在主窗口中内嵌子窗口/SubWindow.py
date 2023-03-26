import tkinter as tk


def CreateWindow(width, height, title):
    root = tk.Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


root = CreateWindow(500, 250, "SubWindow")
canvas = CreateCanvas(root, 0, 0, 500, 250)

canvas.create_line(10, 10, 100, 100, fill="black")
canvas.create_oval(10, 110, 100, 200, fill="white", outline="black")
canvas.create_rectangle(110, 10, 200, 100, fill="white", outline="black")

canvas.create_text(
    (110, 170),
    text="你好，这是子窗口！\nThis is sub window!",
    font=("黑体", 30),
    fill="#000000",
    anchor=tk.W,
    justify=tk.LEFT
)

root.mainloop()
