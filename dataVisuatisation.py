import matplotlib.pyplot  as plt 
from storeData import import_data_handler
from storeData import Database_Manager
import numpy as np
from datetime import datetime
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

#accelerometre charts 
fig = plt.figure()
fig.suptitle('Data Visualisation')

ax=fig.add_subplot(3,3,1)
y = np.array(list(map(lambda ligne: ligne[3], data_acceleration)))
x= np.array(list(map(lambda ligne: ligne[2], data_acceleration)))
ax.axes.get_xaxis().set_visible(False)
ax.set( ylabel='Acceleratio_x',
       title='Acceleration values over time ')
ax.plot(x, y)

def formatDate(str_date):
    format = '%d-%b-%Y %H:%M:%S:%f'
    date = datetime.strptime(str_date, format).strftime('%d-%b %H:%M:%S')
    return date
ay=fig.add_subplot(3,3,4)
y = np.array(list(map(lambda ligne: ligne[4], data_acceleration)))
x= np.array(list(map(lambda ligne: formatDate(ligne[2]), data_acceleration)))
ay.axes.get_xaxis().set_visible(False)
ay.set( ylabel='Acceleratio_y' )
ay.plot(x ,y)

az=fig.add_subplot(3,3,7)
y = np.array(list(map(lambda ligne: ligne[5], data_acceleration)))
x= np.array(list(map(lambda ligne: formatDate(ligne[2]), data_acceleration)))
az.set(xlabel='time ', ylabel='Acceleratio_z')
for tick in az.get_xticklabels():
    tick.set_rotation(45)
    tick.set_ha('right')
az.plot(x ,y)


tmp = fig.add_subplot(3,3,3)
y = np.array(list(map(lambda ligne: ligne[3], data_temperator)))
x= np.array(list(map(lambda ligne: formatDate(ligne[2]), data_temperator)))
tmp.plot(x ,y)
tmp.set(xlabel='time', ylabel='temerature value',
       title='temerature values over time')
for tick in tmp.get_xticklabels():
    tick.set_rotation(90)
    tick.set_ha('right')


hum = fig.add_subplot(3,3,2)
y = np.array(list(map(lambda ligne: ligne[3], data_humidity)))
x= np.array(list(map(lambda ligne: formatDate(ligne[2]), data_humidity)))
hum.plot(x, y)
hum.set(xlabel='time', ylabel='humidity value',
       title='humidity values over time')
for tick in hum.get_xticklabels():
    tick.set_rotation(90)
    tick.set_ha('right')

tmp_pie = fig.add_subplot(3,3,8)
temperature_labels = reduce_function_temperature().keys()
temperature_values = reduce_function_temperature().values()
tmp_pie.pie(temperature_values,labels=temperature_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
tmp_pie.set_title("tempurature")     
tmp_pie.axis('equal')

hum_pie = fig.add_subplot(3,3,9)
humidity_labels = reduce_function_humidity().keys()
humidity_values = reduce_function_humidity().values()
hum_pie.pie(humidity_values,labels=humidity_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)     
hum_pie.axis('equal')
hum_pie.set_title("Humidity")   
plt.show()
