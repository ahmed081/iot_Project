import matplotlib.pyplot  as plt 
from storeData import import_data_handler
from storeData import Database_Manager

#import data from db
data_temperator = import_data_handler("Temperature_Data")
data_humidity = import_data_handler("Humidity_Data")
dbobj = Database_Manager()
data_acceleration = dbobj.select_db_record("select * from Acceleration_Data order by Date_Time")
del dbobj

#preparing data for visialisation 

