import tkinter as tk
import time

def fRename():
    print(ID_entry.get())
def fHang():
    pass
def fA():
    pass
def fB():
    pass
window = tk.Tk()
window.title('學生端')

#ID、rename
ID_label=tk.Label(text="ID:")
ID_entry=tk.Entry(width=10)
ID_label.pack(side='left')
ID_entry.pack(side='left')
rename=tk.Button(text="👣",command=fRename,width=1)
rename.pack(side='right')

#hang
hand_Button=tk.Button(text="舉手",background='gray',command=fHang)
hand_Button.pack(side='left')
A_Button=tk.Button(text="A",background='gray',command=fA)
A_Button.pack(side='left')
B_Button=tk.Button(text="B",background='gray',command=fB)
B_Button.pack(side='left')


window.mainloop()