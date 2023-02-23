import tkinter as tk
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

IDnum='01'
handStatus=0
AStatus=0
BStatus=0


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # 將訂閱主題寫在on_connet中
    # 如果我們失去連線或重新連線時 
    # 地端程式將會重新訂閱
    client.subscribe("pingHandSystem/MQTT")

'''def on_message(client, userdata, msg):
    if(msg.payload.need=='sendStatus'):
        if(msg.payload.info[0]):
            hand_Button.config(background='yellow')
        else:
            hand_Button.config(background='gray')
        if(msg.payload.info[1]):
            A_Button.config(background='yellow')
        else:
            A_Button.config(background='gray')
        if(msg.payload.info[2]):
            B_Button.config(background='yellow')
        else:
            B_Button.config(background='gray')'''
    
client = mqtt.Client()

# 設定連線的動作
client.on_connect = on_connect

# 設定接收訊息的動作
#client.on_message = on_message

# 設定登入帳號密碼
client.username_pw_set("","")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("test.mosquitto.org", 1883, 60)

# 開始連線，執行設定的動作和處理重新連線問題
# 也可以手動使用其他loop函式來進行連接
client.loop_start()

def fRename():
    t={
        'From':'student',
        'to':'lib',
        'ID':IDnum,
        'need':'rename',
        'info':[name_entry.get()]
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
def fHang():
    t={
        'From':'student',
        'to':'lib',
        'ID':IDnum,
        'need':'getAndChangeIDStstus',
        'info':['hand']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
def fA():
    t={
        'From':'student',
        'to':'lib',
        'ID':IDnum,
        'need':'getAndChangeIDStstus',
        'info':['A']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
def fB():
    t={
        'From':'student',
        'to':'lib',
        'ID':IDnum,
        'need':'getAndChangeIDStstus',
        'info':['B']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
window = tk.Tk()
window.title('學生端')

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
B_Button.pack(side='left')


window.mainloop()
