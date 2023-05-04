from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Vito GUI")
root.geometry("320x240")  # 가로 * 세로

values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일')

# 읽기 전용
readonly_combobox = ttk.Combobox(root, height=5, values=values, state='readonly')
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get()) # 선택된 값 표시

btn = Button(root, text='select', command=btncmd)
btn.pack()

root.mainloop()
