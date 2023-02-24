import tkinter


# 計算
def calculate():
    # 計算
    # equ.get()獲取此時equ內容
    # eval  計算
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))


# 將我們的數字打在文本框上
def show(buttonString):
    # 獲取內容
    content = equ.get()
    # 判斷，如果內容爲0的話相當於沒計算，所以空字符串拼接，還是0
    # 如果內容爲10的話，content就爲10，再拼接我們所按的數字
    if content == "0":
        content = ""
    equ.set(content + buttonString)


# 清除，置爲0
def clear():
    equ.set("0")


# 退位
def backSpace():
    # 刪除前一個字符
    equ.set(str(equ.get()[:-1]))


# 更改顏色的方法
def moved(event, i, color):
    i.config(bg=color)


# 使函數傳遞多個參數，lambda只能傳遞一個參數
def handlerAdaptor(fun, **kwds):
    return lambda event, func=fun, kwds=kwds: fun(event, **kwds)


def fun(list):
    for i in list:
        # 試圖獲取bg的屬性值，
        x = i.cget("bg")
        # 當鼠標進入控件時，執行moved操作，變顏色
        i.bind("<Enter>", handlerAdaptor(moved, i=i, color="lightyellow"))
        # 當鼠標移出控件時，執行moved操作，恢復顏色
        i.bind("<Leave>", handlerAdaptor(moved, i=i, color=x))


# 主程序
root = tkinter.Tk()
# 設置程序標題
root.title("簡易計算器")
# 框體可拖拽，0,0表示不能拖拽
root.resizable(0, 0)
# equ 是存放顯示區的數字
equ = tkinter.StringVar()
# 默認爲0
equ.set("0")

# 設置文本框
# width 寬爲25
# height 高爲2
# relief  指
# font指字體這裏我們只設置了字體的大小
label = tkinter.Label(root, width=25, height=2, relief="raised", anchor=tkinter.SE, textvariable=equ)
# row  指entry組件在網格中的橫向位置
# column  指entry組件在網格中的縱向位置
# columnspan  指設定entry組件在column方向的合併數量
# padx/pady  設定組件邊界與容器(可想成窗口邊界)的距離或是控件邊界間的距離
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# row1的按鈕

# 清除顯示區按鈕AC
buttonClear = tkinter.Button(root, text="AC", width=5, bg="#ff6348", command=clear)
buttonClear.grid(row=1, column=0)

# 退位鍵按鈕
buttonBack = tkinter.Button(root, text="<-", width=5, bg="#ff6348", command=backSpace)
buttonBack.grid(row=1, column=1)

# 餘按鈕
buttonYu = tkinter.Button(root, text="%", width=5, bg="lightblue", command=lambda: show("%"))
buttonYu.grid(row=1, column=2)

# 除按鈕
buttonDivision = tkinter.Button(root, text="/", width=5, bg="lightblue", command=lambda: show("/"))
buttonDivision.grid(row=1, column=3)

# row2的按鈕

# 數字7
button7 = tkinter.Button(root, text="7", width=5, bg="orange", command=lambda: show("7"))
button7.grid(row=2, column=0)

# 數字8
button8 = tkinter.Button(root, text="8", width=5, bg="orange", command=lambda: show("8"))
button8.grid(row=2, column=1)

# 數字9
button9 = tkinter.Button(root, text="9", width=5, bg="orange", command=lambda: show("9"))
button9.grid(row=2, column=2)

# 乘法按鈕
buttonMultiplication = tkinter.Button(root, text="*", width=5, bg="lightblue", command=lambda: show("*"))
buttonMultiplication.grid(row=2, column=3)

# row3的按鈕

# 數字4
button4 = tkinter.Button(root, text="4", width=5, bg="orange", command=lambda: show("4"))
button4.grid(row=3, column=0)

# 數字5
button5 = tkinter.Button(root, text="5", width=5, bg="orange", command=lambda: show("5"))
button5.grid(row=3, column=1)

# 數字6
button6 = tkinter.Button(root, text="6", width=5, bg="orange", command=lambda: show("6"))
button6.grid(row=3, column=2)

# 減法按鈕
buttonSubtraction = tkinter.Button(root, text="-", width=5, bg="lightblue", command=lambda: show("-"))
buttonSubtraction.grid(row=3, column=3)

# row4的按鈕

# 數字1
button1 = tkinter.Button(root, text="1", width=5, bg="orange", command=lambda: show("1"))
button1.grid(row=4, column=0)

# 數字2
button2 = tkinter.Button(root, text="2", width=5, bg="orange", command=lambda: show("2"))
button2.grid(row=4, column=1)

# 數字3
button3 = tkinter.Button(root, text="3", width=5, bg="orange", command=lambda: show("3"))
button3.grid(row=4, column=2)

# 加法按鈕
buttonAdd = tkinter.Button(root, text="+", width=5, bg="lightblue", command=lambda: show("+"))
buttonAdd.grid(row=4, column=3)

# row5的按鈕

# 小數點按鈕
buttonPoint = tkinter.Button(root, text=".", width=5, bg="orange", command=lambda: show("."))
buttonPoint.grid(row=5, column=0)

# 數字0
button0 = tkinter.Button(root, text="0", width=5, bg="orange", command=lambda: show("0"))
button0.grid(row=5, column=1)

# 等於號
buttonEqual = tkinter.Button(root, text="=", width=12, bg="lightgreen", command=calculate)
buttonEqual.grid(row=5, column=2, columnspan=2)

# 各個選項的變量名
list = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0,
        buttonAdd, buttonSubtraction, buttonMultiplication, buttonDivision, buttonPoint,
        buttonEqual, buttonYu, buttonClear, buttonBack]

fun(list)

# 程序循環進行
root.mainloop()