from tkinter import *

root = Tk()
root.title("Vito GUI")
root.geometry("320x240")  # 가로 * 세로

Label(root, text='메뉴를 선택하세요').pack()

burger_var = IntVar()  # 여기에 int 형으로 값을 저장함
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='불고기버거', value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text='음료를 선택하세요').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='아이스티', value='아이스티', variable=drink_var)
btn_drink3 = Radiobutton(
    root, text='오렌지 주스', value='오렌지 주스', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())


btn = Button(root, text='order', command=btncmd)
btn.pack()

root.mainloop()
