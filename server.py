import paho.mqtt.client as mqtt
import sqlite3
db=sqlite3.connect('lib.db')
cursor=db.cursor()
import json

def reuturnReset():
    for i in range(1,31):
        a='select * from status where ID=%d'%(i)
        cursor.execute(a)
        x=cursor.fetchone()
        print(x)
        t={
            'From':'lib',
            'to':'teacher',
            'ID':x[0],
            'need':'returnReset',
            'info':x
        }
        client.publish("pingHandSystem/MQTT",json.dumps(t))
        print(json.dumps(t))
        print(x)

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
            try:
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
            except:
                pass
        elif(getmsg["info"][0]=='A'):
            try:
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
            except:
                pass
        elif(getmsg["info"][0]=='B'):
            try:
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
            except:
                pass
        try:
            a="select handStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x=[cursor.fetchone()[0],0,0]
            a="select AStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x[1]=cursor.fetchone()[0]
            a="select BStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x[2]=cursor.fetchone()[0]
            t={
                'From':'server',
                'to':'student',
                'ID':getmsg["ID"],
                'need':'sendStatus',
                'info':x
            }
            client.publish("pingHandSystem/MQTT",json.dumps(t))
            reuturnReset()
        except:
            pass

    if(getmsg["need"]=='rename'):
        try:
            a="update status set name='%s' where ID == '%s'"%(getmsg['info'][0],getmsg["ID"])
            cursor.execute(a)
            db.commit()
            reuturnReset()
        except:
            pass
    if(getmsg["need"]=='allRelax'):
        print("allRelax")
        try:
            if(getmsg['info'][0]=='hand'):
                a="update status set handStatus=0"
                cursor.execute(a)
                db.commit()
            elif(getmsg['info'][0]=='A'):
                a="update status set AStatus=0"
                cursor.execute(a)
                db.commit()
            elif(getmsg['info'][0]=='B'):
                a="update status set BStatus=0"
                cursor.execute(a)
                db.commit()
            a="select handStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x=[cursor.fetchone()[0],0,0]
            a="select AStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x[1]=cursor.fetchone()[0]
            a="select BStatus from status where ID=='%s'"%(getmsg["ID"])
            cursor.execute(a)
            x[2]=cursor.fetchone()[0]
            t={
                'From':'server',
                'to':'student',
                'ID':getmsg["ID"],
                'need':'sendStatus',
                'info':x
            }
            client.publish("pingHandSystem/MQTT",json.dumps(t))
            reuturnReset()
        except:
            pass
    if(getmsg["need"]=='reset'):
        reuturnReset()
            #print(type(x[0]))
        

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