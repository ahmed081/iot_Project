import json 
import sqlite3


db_name = "IoT_DataBase.db"

class Database_Manager():

    def __init__(self):
        self.conn = sqlite3.connect(db_name,isolation_level=None)
        self.cur = self.conn.cursor() 

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args) 
        print("insert .......................")
        return

    def select_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args) 
        
        return self.cur.fetchall()
    
    def _del_(self):
        self.cur.close() 
        self.conn.close()

    @staticmethod
    def getDataSet(sqlText):
        #Push into DB Table 
        dbobj = Database_Manager() 
        rows=dbobj.select_db_record(sqlText) 
        del dbobj
        return rows

# Function to save Temperature to DB Table 51 
def Temperature_Data_Handler(json_Data):
    #Parse Data 
    json_Dict = json.loads(json_Data) 
    SensorID = json_Dict['Sensor_ID'] 
    Date_Time = json_Dict['Date_Time'] 
    Temperature = float(json_Dict['Temperature'])
    TemperatureLevel = json_Dict['TemperatureLevel']

    #Push into DB Table

    dbobj = Database_Manager()
    dbobj.add_del_update_db_record("insert into Temperature_Data (Sensor_ID,Date_Time,Temperature,TemperatureLevel)values (?,?,?,?)",
            [SensorID,Date_Time,Temperature,TemperatureLevel])
    del dbobj 

    print ("Inserted Temperature Data into Database.") 
    print ("")


 # Function to save Acceleration to DB Table 67 
def Acceleration_Data_Handler(json_Data):
    json_Dict = json.loads(json_Data) 
    SensorID = json_Dict['sensor_ID'] 
    Date_Time = json_Dict['Date_Time'] 
    print(' ****** ',Date_Time) 
    accx = float(json_Dict['cc']) 
    accy = float(json_Dict['accy']) 
    accz = float(json_Dict['accz']) 
    #Push into The Table 
    dbobj = Database_Manager() 
    dbobj.add_del_update_db_record("insert into Acceleration_Data (SensorID,Date_Time,cc,accy,accz) values (?,?,?,?)",
        [SensorID,Date_Time,accx,accy,accz])
    del dbobj 
    print("Inserted Acceleration Data into Database.") 
    print ("")

 # Function to save Humidity to DB Table 
def Humidity_Data_Handler(json_Data):
    
    json_Dict = json.loads(json_Data) 
    print("humidity here ............. " )
    print((json_Dict['Sensor_ID'] ))
    SensorID = json_Dict['Sensor_ID'] 
    Date_Time = json_Dict['Date_Time']
    HumidityLevel = json_Dict['HumidityLevel'] 
    Humidity = float(json_Dict['Humidity']) 
    #Push into The Table 
    
    dbobj = Database_Manager() 
    
    dbobj.add_del_update_db_record("insert into Humidity_Data (SensorID,Date_Time,HumidityLevel,Humidity) values (?,?,?,?)"
        ,[SensorID,Date_Time,HumidityLevel,Humidity])
    
    del dbobj 
    print("Inserted Humidity Data into Database.") 
    print ("")
#Master function to select DB Function based on MQTT Topic
def sensor_Data_Handler(Topic, json_Data):
    print("topickkkkk : "+Topic)
    if Topic == "Home/BedRoom/DHT1/Temperature":
        Temperature_Data_Handler(json_Data) 
    elif Topic == "Home/BedRoom/DHT1/Humidity":
        Humidity_Data_Handler(json_Data) 
    elif Topic == "Home/BedRoom/DHT1/Acceleration":
        Acceleration_Data_Handler(json_Data)