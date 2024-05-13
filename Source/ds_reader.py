'''
DS18B20 tools
by: JOR 2024
Alpha version:  12MAY24
Based on code by Scott Campbell, Circuit Basics
'''

import time

def read_temp_raw(devicefile):
    f = open(devicefile, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(devicefile):
    # Get the two lines returned by sensor
    lines = read_temp_raw(devicefile)
    # Check for the CRC at the end of line 1
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(devicefile)
    # Find where the temperature starts
    equals_pos = lines[1].find('t=')
    # If this is a valid value
    if equals_pos != -1:
        # The string starts at the equal sign and runs to the end
        temp_string = lines[1][equals_pos+2:]
        # Convert to float and divide by 100
        temp_c = float(temp_string) / 1000.0
        return temp_c