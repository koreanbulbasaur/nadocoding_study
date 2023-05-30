from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Vito GUI")
root.geometry("320x240")  # 가로 * 세로

Label(root, text='메뉴를 선택해 주세요').pack(side='top')

Button(root, text='order').pack(side='bottom')

# 메뉴 프레임
frame_burger = Frame(root, relief='solid', bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text = 'hamburger').pack()
Button(frame_burger, text = 'chesse_hamburger').pack()
Button(frame_burger, text = 'Bulgogi_hamburger').pack()

# 음료 프레임
frmae_drink = LabelFrame(root, text='음료')
frmae_drink.pack(side='right', fill='both', expand=True)

Button(frmae_drink, text = 'coke').pack()
Button(frmae_drink, text = 'icetea').pack()

root.mainloop()
