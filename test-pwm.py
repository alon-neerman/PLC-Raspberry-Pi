#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import os
from PLC import PLC

while True:
    try:
        client = PLC(plc_name='M172', host='192.168.1.200', port='502')
        print(client.read_analog_input(3))
    except:
        print("broken")
