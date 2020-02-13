import sys
from tkinter import messagebox

sys.path.append(sys.path[0] + "\\window")
import MainWindows


def start():
    if __name__ == "__main__":
        MainWindows.callWin()
    else:
        messagebox.showinfo("启动失败", "启动参数校验错误")


start()
