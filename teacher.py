import tkinter as tk
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

IDnum=1

status=[[]*5]*30
print(status)

def reset():
    t={
        'From':'teacher',
        'to':'lib',
        'ID':IDnum,
        'need':'reset',
        'info':['A']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # 將訂閱主題寫在on_connet中
    # 如果我們失去連線或重新連線時
    # 地端程式將會重新訂閱
    client.subscribe("pingHandSystem/MQTT")

def on_message(client, userdata, msg):
    print('getmsg')
    getmsg=json.loads(str(msg.payload)[2:-1])
    if(getmsg["need"]=='returnReset'):
        name_Label[getmsg["info"][0]-1].config(text=getmsg["info"][1])
        hand_Label[getmsg["info"][0]-1].config(text='舉手'+str(getmsg["info"][2]))
        A_Label[getmsg["info"][0]-1].config(text='A'+str(getmsg["info"][3]))
        B_Label[getmsg["info"][0]-1].config(text='B'+str(getmsg["info"][4]))
    
client = mqtt.Client()

# 設定連線的動作
client.on_connect = on_connect

# 設定接收訊息的動作
client.on_message = on_message

# 設定登入帳號密碼
client.username_pw_set("","")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("test.mosquitto.org", 1883, 60)

# 開始連線，執行設定的動作和處理重新連線問題
# 也可以手動使用其他loop函式來進行連接
client.loop_start()

window = tk.Tk()
window.title('老師端')

count=0
group=[]
ID_Label=[]
name_Label=[]
hand_Label=[]
A_Label=[]
B_Label=[]
for i in range(0,10):
    for j in range(0,3):
        group.insert(count,tk.LabelFrame(window, text=(count+1), width=400, height=40))
        group[count].grid(row=i,column=j)
        ID_Label.insert(count,tk.Label(group[count],text='ID:'+str(count+1)))
        ID_Label[count].pack(side="left")

        name_Label.insert(count,tk.Label(group[count],text=''))
        name_Label[count].pack(side="left")

        hand_Label.insert(count,tk.Label(group[count],text='舉手'))
        hand_Label[count].pack(side="left")

        A_Label.insert(count,tk.Label(group[count],text='A'))
        A_Label[count].pack(side="left")

        B_Label.insert(count,tk.Label(group[count],text='B'))
        B_Label[count].pack(side="left")

        count+=1

rename=tk.Button(text="👣",command=reset,width=1)
rename.place(relx=0.9,rely=0.9)

'''
#ID、rename
ID_label=tk.Label(text="ID:%s"%(IDnum))
name_entry=tk.Entry(width=10)
ID_label.pack(side='left')
name_entry.pack(side='left')
rename=tk.Button(text="👣",command=fRename,width=1)
rename.pack(side='right')

#hang
hand_Button=tk.Button(text="舉手",background='gray',command=fHang)
hand_Button.pack(side='left')
A_Button=tk.Button(text="A",background='gray',command=fA)
A_Button.pack(side='left')
B_Button=tk.Button(text="B",background='gray',command=fB)
B_Button.pack(side='left')'''


window.mainloop()