"""
本代码由[Tkinter布局助手]生成
当前版本:3.1.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *

"""
全局通用函数
"""


# 自动隐藏滚动条
def scrollbar_autohide(bar, widget):
    def show():
        bar.lift(widget)

    def hide():
        bar.lower(widget)

    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lfourdxk = self.__tk_label_lfourdxk()
        self.tk_button_lfouroga = self.__tk_button_lfouroga()
        self.tk_input_lfous2wb = self.__tk_input_lfous2wb()
        self.tk_text_lfousr5x = self.__tk_text_lfousr5x()
        self.tk_radio_button_lfout19d = self.__tk_radio_button_lfout19d()
        self.tk_check_button_lfout6fi = self.__tk_check_button_lfout6fi()
        self.tk_list_box_lfoutd1y = self.__tk_list_box_lfoutd1y()
        self.tk_select_box_lfoutr5h = self.__tk_select_box_lfoutr5h()
        self.tk_progressbar_lfouu0e5 = self.__tk_progressbar_lfouu0e5()
        self.tk_table_lfouukil = self.__tk_table_lfouukil()
        self.tk_frame_lfouusqx = Frame_lfouusqx(self)
        self.tk_label_frame_lfouv63w = Frame_lfouv63w(self)
        self.tk_tabs_lfouvm6x = Frame_lfouvm6x(self)
        self.tk_button_lfouvyb2 = self.__tk_button_lfouvyb2()

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 820
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_lfourdxk(self):
        label = Label(self, text="标签", anchor="center")
        label.place(x=620, y=340, width=180, height=139)
        return label

    def __tk_button_lfouroga(self):
        btn = Button(self, text="按钮")
        btn.place(x=220, y=20, width=180, height=141)
        return btn

    def __tk_input_lfous2wb(self):
        ipt = Entry(self)
        ipt.place(x=420, y=20, width=180, height=139)
        return ipt

    def __tk_text_lfousr5x(self):
        text = Text(self)
        text.place(x=20, y=180, width=180, height=139)

        return text

    def __tk_radio_button_lfout19d(self):
        rb = Radiobutton(self, text="单选框")
        rb.place(x=220, y=180, width=179, height=60)
        return rb

    def __tk_check_button_lfout6fi(self):
        cb = Checkbutton(self, text="多选框")
        cb.place(x=220, y=261, width=180, height=59)
        return cb

    def __tk_list_box_lfoutd1y(self):
        lb = Listbox(self)
        lb.insert(END, "列表框")
        lb.insert(END, "Python")
        lb.insert(END, "Tkinter Helper")
        lb.place(x=420, y=180, width=179, height=139)

        return lb

    def __tk_select_box_lfoutr5h(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("列表框", "Python", "Tkinter Helper")
        cb.place(x=20, y=340, width=181, height=61)
        return cb

    def __tk_progressbar_lfouu0e5(self):
        progressbar = Progressbar(self, orient=HORIZONTAL)
        progressbar.place(x=20, y=420, width=180, height=59)
        return progressbar

    def __tk_table_lfouukil(self):
        # 表头字段 表头宽度
        columns = {"ID": 35, "字段#1": 53, "字段#2": 89}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        tk_table.place(x=220, y=340, width=180, height=141)

        return tk_table

    def __tk_button_lfouvyb2(self):
        btn = Button(self, text="按钮")
        btn.place(x=20, y=20, width=181, height=140)
        return btn


class Frame_lfouusqx(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.place(x=420, y=340, width=179, height=140)


class Frame_lfouv63w(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.configure(text="标签容器")
        self.place(x=620, y=20, width=177, height=139)


class Frame_lfouvm6x(Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.tk_tabs_lfouvm6x_0 = Frame_lfouvm6x_0(self)
        self.add(self.tk_tabs_lfouvm6x_0, text="选项卡1")

        self.tk_tabs_lfouvm6x_1 = Frame_lfouvm6x_1(self)
        self.add(self.tk_tabs_lfouvm6x_1, text="选项卡2")

        self.place(x=620, y=180, width=180, height=140)


class Frame_lfouvm6x_0(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.place(x=620, y=180, width=180, height=140)


class Frame_lfouvm6x_1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.place(x=620, y=180, width=180, height=140)


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()
