import paho.mqtt.client as mqtt
import sqlite3
db=sqlite3.connect('lib.db')
cursor=db.cursor()
import json

# 當地端程式連線伺服器得到回應時，要做的動作
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # 將訂閱主題寫在on_connet中
    # 如果我們失去連線或重新連線時 
    # 地端程式將會重新訂閱
    client.subscribe("pingHandSystem/MQTT")

# 當接收到從伺服器發送的訊息時要進行的動作
def on_message(client, userdata, msg):
    getmsg=json.loads(str(msg.payload)[2:-1])
    print(getmsg)
    print(getmsg,type(getmsg))
    if(getmsg["need"]=='getAndChangeIDStstus'):
        print('need')
        if(getmsg["info"][0]=='hand'):
            print('hand')
            a="select handStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            if(cursor.fetchone()[0]):
                a="update status set handStatus=0 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()
            else:
                a="update status set handStatus=1 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()
        elif(getmsg["info"][0]=='A'):
            a="select AStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            
            if(cursor.fetchone()[0]):
                a="update status set AStatus=0 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()
            else:
                a="update status set AStatus=1 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()
        elif(getmsg["info"][0]=='B'):
            a="select BStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            if(cursor.fetchone()[0]):
                a="update status set BStatus=0 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()
            else:
                a="update status set BStatus=1 where ID == '%s'"%(getmsg["ID"])
                cursor.execute(a)
                db.commit()

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定連線的動作
client.on_connect = on_connect

# 設定接收訊息的動作
client.on_message = on_message

# 設定登入帳號密碼
client.username_pw_set("","")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()