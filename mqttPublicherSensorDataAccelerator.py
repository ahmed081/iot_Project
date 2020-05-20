import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

import re 
from time import sleep
from pynput import keyboard
import socket,traceback
import time

def on_connect(client, userdata, rc):
    if rc != 0:
        pass
        print ("Unable to connect to MQTT Broker...")
    else:
        print ("Connected with MQTT Broker: " + str(MQTT_Broker))
def on_publish(client, userdata, mid):
    pass
def on_disconnect(client, userdata, rc):
    if rc !=0:
        pass
def publish_To_Topic(topic, message):
    mqttc.publish(topic,message)
    print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
    print ("")

break_Program = False
def onPress(key):
    global break_Program
    if key == keyboard.Key.end:
        print('end pressed')
        break_Program
        return False
def mapMessageToJson(msg,addr):
        disc = {}
        lst = re.split("[,\']",str(msg))
        disc['sensor_ID'] = "acceleration-Sensor1"
        disc['Date_Time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
        disc['accX'] = lst[3].strip()
        disc['accY'] = lst[4].strip()
        disc['accZ'] = lst[5].strip()   
        return json.dumps(dict)   
# MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 30
MQTT_Topic_Acceleration = "Home/BedRoom/DHT1/Acceleration"
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
host = ''
port = 5555
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.bind((host,port))
dic={}
with keyboard.Listener(on_press = onPress) as listener:
    
    while break_Program == False:
        try:
            
            message,address = s.recvfrom(8192)
            print("here")
            acceleration_Json_Data = mapMessageToJson(message,address)
            publish_To_Topic (MQTT_Topic_Acceleration,acceleration_Json_Data)
            if address not in dic:
                dic[address]=List()
                dic[address].append(acceleration_Json_Data)
            else:
                dic[address].append(acceleration_Json_Data)
            print(address , "    ",acceleration_Json_Data)
            sleep(1)
        except:
            traceback.print_exc()
        listener.join()
#python mqttPublicherSensorDataAccelerator.py