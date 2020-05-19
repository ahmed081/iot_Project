import sqlite3
DB_Name = "IoT_DataBase.db"
TableSchema=""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
cursor = conn.cursor()

#Create Tables
cursor.execute("CREATE TABLE IF NOT EXISTS  Temperature_Data (\
    id integer primary key autoincrement,\
    SensorID text,\
    Date_Time text,\
    Temperature decimal(6,2),\
    TemperatureLevel text\
    )"
)

cursor.execute("CREATE TABLE IF NOT EXISTS  Humidity_Data (\
    id integer primary key autoincrement,\
    SensorID text, Date_Time text,\
    Humidity decimal(6,2),\
    HumidityLevel text\
    )"
)

cursor.execute("CREATE TABLE IF NOT EXISTS  Acceleration_Data (\
    id integer primary key autoincrement,\
    SensorID text,\
    Date_Time text, accX decimal(6,2),\
    accY decimal(6,2), accZ decimal(6,2)\
    )"
)
#Close DB
cursor.close()
conn.close()




