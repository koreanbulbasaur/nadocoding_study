from tkinter import *

root = Tk()
root.title("Vito GUI")
root.geometry("320x240")  # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0)  # 복수 선택
# listbox = Listbox(root, selectmode="single", height=0) # 단수 선택
# listbox = Listbox(root, selectmode="single", height=3)  # 값을 3개만 보여줌
listbox.insert(0, "망고스틴")
listbox.insert(1, "망고")
listbox.insert(2, '수박')
listbox.insert(END, '바나나')
listbox.insert(END, '용과')
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(END)  # 맨 뒤에 항목을 삭제
    # listbox.delete(0)  # 맨 앞에 항목을 삭제

    # 갯수 확인
    # print('리스트에는', listbox.size(), '개가 있어요')

    # 항목 확인 (시작 idx, 끝 idx)
    # print('1번째부터 3번째까지의 항목 :', listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 :", listbox.curselection())


btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()
