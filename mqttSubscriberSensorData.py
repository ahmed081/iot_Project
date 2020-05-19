import paho.mqtt.client as mqtt from storeData 
import sensor_Data_Handler


#Subscribe to all Sensors at Base Topic 
def on_connect(mosq, obj, rc):
    if rc==0:
        print("connected") mgttc.subscribe(MQTT Topic, 0)
    else:
        print("bad connection")
#Save Data into DB Table

def on_message(imas, abj, msg):
    print ("MQTT Data Received...") 
    print ("MQTT Topic: " msg.topic) 
    print ("Data:" + str(msg.payload)) 
    sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_gos):
    # MQTT Settings 33 
    MQTT_Broker = "mqtt.eclipse.org"
    MQTT Port = 1883 35 Keep Alive Interval = 30