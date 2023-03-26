import tkinter as tk
from tkinter import PhotoImage


def CreateWindow(width, height, title):
    root = tk.Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


root = CreateWindow(1000, 500, "ChessUI")
canvas = CreateCanvas(root, 0, 0, 1000, 500)

# canvas.create_line(x1, y1, x2, y2, fill="black")
# canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
# canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

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

root.mainloop()
