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

def on_message(client, userdata, msg):
    pass
    
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

def fHang():
    t={
        'From':'control',
        'to':'lib',
        'ID':IDnum,
        'need':'allRelax',
        'info':['hand']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
def fA():
    t={
        'From':'control',
        'to':'lib',
        'ID':IDnum,
        'need':'allRelax',
        'info':['A']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
def fB():
    t={
        'From':'control',
        'to':'lib',
        'ID':IDnum,
        'need':'allRelax',
        'info':['B']
    }
    client.publish("pingHandSystem/MQTT",json.dumps(t))
window = tk.Tk()
window.title('控制端')


#hang
hand_Button=tk.Button(text="舉手",background='gray',command=fHang,width=10,height=10,)
hand_Button.pack(side='left')
A_Button=tk.Button(text="A",background='gray',command=fA,width=10,height=10)
A_Button.pack(side='left')
B_Button=tk.Button(text="B",background='gray',command=fB,width=10,height=10)
B_Button.pack(side='left')


window.mainloop()
