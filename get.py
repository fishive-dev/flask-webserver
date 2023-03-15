'''
This custom library contains functions to simulate 
data retrieval from sensors on the Raspberry Pi
'''

import random
import time
import json

# global variables
feed_times = [                  # fish are fed thrice a day at these specific times [Hrs,Min,Sec]
    [22,0,0], 
    [14,0,0], 
    [6,0,0]
]


'''
methods to retrieve data selectively - 
sensors only
status only
all data
'''
# Get all data in json format
def json_all():
    out = json.dumps(indent = 4, obj = {
        'temp1':temp1(),
        'temp2':temp2(),
        'light':light(),
        'cur_time':cur_time(),
        'last_feed':last_feed(),
        'filter_status':filter_status(),
        'pump_status':pump_status(),
        'light_status':light_status(),
        'rgba_val':rgba_val()
    })
    return out

# Get only sensor data in json format
def json_sensor():
    out = json.dumps(indent = 4, obj = {
        'temp1':temp1(),
        'temp2':temp2(),
        'light':light()
    })
    return out

# Get only device status in json format
def json_status():
    out = json.dumps(indent = 4, obj = {
        'filter_status':filter_status(),
        'pump_status':pump_status(),
        'light_status':light_status()
    })
    return out


'''
Sensor data retrieval functions
'''
# Temperature sensor 1 (Celsius)
def temp1():
    out = random.randint(23,29)
    return out

# Temperature sensor 2 (Celsius)
def temp2():
    out = random.randint(23,29)
    return out

# Ambient light sensor (Lumen)
def light():
    out = random.randint(10,60)
    return out


'''
Time retrieval functions
'''
# Current system time
def cur_time():
    t = time.localtime()
    out = [t.tm_hour, t.tm_min, t.tm_sec]
    return out

# Time since last feed
def last_feed():
    global feed_times 
    t = time.localtime()
    if t.tm_hour >= 22:
        out = [
            t.tm_hour - feed_times[0][0],
            t.tm_min - feed_times[0][1],
            t.tm_sec - feed_times[0][2]
        ]
    elif t.tm_hour >= 14:
        out = [
            t.tm_hour - feed_times[1][0],
            t.tm_min - feed_times[1][1],
            t.tm_sec - feed_times[1][2]
        ]
    elif t.tm_hour >= 6:
        out = [
            t.tm_hour - feed_times[2][0],
            t.tm_min - feed_times[2][1],
            t.tm_sec - feed_times[2][2]
        ]
    else:
        out = [
            t.tm_hour + (24 - feed_times[0][0]),
            t.tm_min + (60 - feed_times[0][1]),
            t.tm_sec + (60 - feed_times[0][2])
        ]
    return out


'''
Device status functions
'''
# Filter status (ON/OFF)
def filter_status():
    out = random.choice([0,1])
    return out

# Pump status (ON/OFF)
def pump_status():                              
    out = random.choice([0,1])
    return out

# Lights status
def light_status():
    out = random.choice([0,1])
    return out


'''
Miscellaneous functions
'''
# Light RGB color
def rgba_val():
    hex = "".join(random.choices("ABCDEF0123456789", k = 6))
    alpha = round(random.random(),2)
    out = [hex, alpha]
    return out