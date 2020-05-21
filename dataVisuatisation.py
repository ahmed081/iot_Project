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


def map_function_temperature(temperature_data):
    return [temperature_data[4] , temperature_data[3]]

def map_function_Humidity(humidity_data):
    return [humidity_data[4] , humidity_data[3]]
def map_function_Accelerator(accelerator_data):
    return [accelerator_data[3] , accelerator_data[4],accelerator_data[4]]


def reduce_function_temperature():
    data_temperature = list(map(map_function_temperature, data_temperator))
    disc_temp = dict()
    for element in data_temperature :
        if element[0] not in disc_temp :
            disc_temp[element[0]] = element[1]
        else: 
            disc_temp[element[0]] += element[1]
    return disc_temp



def reduce_function_humidity():
    data_humidityy = list(map(map_function_Humidity, data_humidity))
    disc_h = dict()
    for element in data_humidityy :
        if element[0] not in disc_h :
            disc_h[element[0]] = element[1]
        else: 
            disc_h[element[0]] += element[1]
    return disc_h
data_acceleration = list(map(map_function_Accelerator, data_acceleration))



#graph manipulation
print(reduce_function_temperature())
print(reduce_function_humidity())
print(data_acceleration)