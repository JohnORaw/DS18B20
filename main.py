#!/usr/bin/env python3

'''
DS18B20 tools
by: JOR 2024
Alpha version:  12MAY24
'''

import os
import time
from Source.ds_reader import read_temp
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

if __name__=="__main__":

    base_dir = '/sys/bus/w1/devices/'
    
    for devicename in os.listdir('/sys/bus/w1/devices/'):
        if devicename == 'w1_bus_master1':
            pass
        else:
            devicefile = base_dir + devicename + '/w1_slave'
            print(f"Sensor {devicename} has a temperature of {read_temp(devicefile)} C")