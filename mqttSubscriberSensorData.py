import paho.mqtt.client as mqtt 
from storeData import sensor_Data_Handler


#Subscribe to all Sensors at Base Topic 
def on_connect(mosq, obj, rc):
    if rc==0:
        print("connected") 
        mqttc.subscribe(MQTT_Topic, 0)
    else:
        print("bad connection")
#Save Data into DB Table

def on_message(imas, abj, msg):
    print ("MQTT Data Received...") 
    print ("MQTT Topic: " +msg.topic) 
    print ("Data:" + str(msg.payload)) 
    sensor_Data_Handler((msg.topic).strip(), msg.payload)


def on_subscribe(mosq, obj, mid, granted_gos):
    pass
# MQTT Settings 
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883 
Keep_Alive_Interval = 30
MQTT_Topic = "Home/BedRoom/#"
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
# Connect & subscribe
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.subscribe(MQTT_Topic, 0)
print("lancement")
mqttc.loop_forever() # Continue the network loop

