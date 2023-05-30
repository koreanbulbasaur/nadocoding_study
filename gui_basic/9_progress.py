from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Vito GUI")
root.geometry("320x240")  # 가로 * 세로

'''
progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode='determinate')
progressbar2.start(10) # 10 ms 마다 움직임
progressbar2.pack()

def btncmd():
    progressbar.stop()
    progressbar2.stop()

btn = Button(root, text='select', command=btncmd)
btn.pack()
'''

progressbar3 = ttk.Progressbar(root,maximum=100, length=200)
progressbar3.pack()

p_var2 = DoubleVar()
progressbar4 = ttk.Progressbar(root,maximum=100, length=200, variable=p_var2)
progressbar4.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.05)

        p_var2.set(i)
        progressbar4.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text='select', command=btncmd2)
btn.pack()

root.mainloop()
