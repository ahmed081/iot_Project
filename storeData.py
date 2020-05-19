import json 
import sqlite3


db_name = "iot_DataBase.db"

class Database_Manager():

    def __init__(self):
        self.conn = sqlite3.connect(DB_Name) 
        self.conn.execute('pragma foreign_keys = on') 
        self.conn.commit() 
        self.cur = self.conn.cursor() 

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args) 
        self.conn.commit() 
        return

    def select_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args) 
        self.conn.commit() 
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
        return rowS

# Function to save Temperature to DB Table 51 
def Temperature_Data_Handler(json_Data):
    #Parse Data 
    json_Data = json.loads(json_Data) 
    SensorID = json_Dict['Sensor_ID'] 
    DateTime = json_Dict['Date'] 
    Temperature = float(json_Dict['Temperature'])
    TemperatureLevel = json_Dict['TemperatureLevel']

    #Push into DB Table

    dbobj = Database_Manager()
    dbobj.add_del_update_db_record("""insert into Temperature_Data (Sensor_ID,Date,Temperature,TemperatureLevel)values 
            ("""+SensorID+","+DateTime+","+DateTime+","+Temperature+")")
    del doby

    print ("Inserted Temperature Data into Database.") 
    print ("")


 # Function to save Acceleration to DB Table 67 
def Acceleration_Data_Handler(json_Data):
    json_Dict = json.loads(jsonData) 
    SensorID = json_Dict['sensor_ID'] 
    DateTime = json_Dict['Date'] 
    print(' ****** ',Date_Time) 
    accx = float(json_Dict['cc']) 
    accy = float(json_Dict['accy']) 
    accz = float(json_Dict['accz']) 
    #Push into The Table 
    dbobj = DatabaseManager() 
    dbobj.add_del_update_db_record("""insert into Acceleration_Data (SensorID,Date,cc,accy,accz) values ("""
        +SensorID+","+DateTime+","+accx+","+accy+","+accz+")"
    ) 
    del dbobj 
    print("Inserted Acceleration Data into Database.") 
    print ("")

 # Function to save Humidity to DB Table 
def Humidity_Data_Handler(json_Data):
    json_Dict = json.loads(jsonData) 
    SensorID = json_Dict['sensor_ID'] 
    Date_Time = json_Dict['Date_Time'] 
    HumidityLevel = json_Dict['HumidityLevel'] 
    Humidity = float(json_Dict['Humidity']) 
    #Push into The Table 
    dbobj = DatabaseManager() 
    dbobj.add_del_update_db_record("""insert into Humidity_Data (SensorID,Date_Time,HumidityLevel,Humidity) values ("""
        +SensorID+","+Date_Time+","+HumidityLevel+","+Humidity+")"
    ) 
    del dbobj 
    print("Inserted Humidity Data into Database.") 
    print ("")
#Master function to select DB Function based on MQTT Topic
def sensor_Data_Handler(Topic, json_Data):
    if Topic == "Home/BedRoom/DHT1/Temperature":
        Temperature_Data_Handler(json_Data) 
    elif Topic == "Home/Bedroom/DHT1/Humidity":
        Humidity_Data_Handler(json_Data) 
    elif Topic == "Home/BedRoom/DHT1/Acceleration":
        Acceleration_Data_Handler(json_Data)