from tkinter import *

root = Tk()
root.title("Vito GUI")
# root.geometry("640x480")  # 가로 * 세로
root.geometry("640x480+100+300")  # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)  # 창 크기 변경 불가

root.mainloop()
