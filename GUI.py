#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

from PLC import PLC
import PySimpleGUI as sg

layout = [[sg.Text('Please enter the PLC Name you want to use: ')],      
                 [sg.Combo(['M172'], key='-PLC-')],
                 [sg.Text('Please enter the IP Address you want to access ')],
                 [sg.InputText(key='-IP-')],
                 [sg.Text('Please enter the port of the device ')],
                 [sg.InputText(key='-Port-')],
                 [sg.Submit(button_text="Connect"), sg.Exit()]]      

window = sg.Window('PLC Project', layout)    

event, values = window.read()    
window.close()

if(event == None or event == "Exit"):exit()

PLC_name = values['-PLC-']    
IP_Addr = values['-IP-']
Port = values['-Port-']
client = PLC(plc_name=PLC_name, host=IP_Addr, port=Port)

while True:
    layout = [      [sg.Text('Please select the function to use')],
                    [sg.Combo(['read_analog_input', 'read_digital_input', "write_digital_output", "read_digital_output"], key='-function-')],
                    [sg.Text('Please enter the IO port you want to access ')],
                    [sg.InputText(key='-IO-')],
                    [sg.Text('(For digital output only!!) Relay on or off?')],
                    [sg.Combo(['on', 'off'], key='-Relay-')],
                    [sg.Submit(), sg.Exit()]] 

    window = sg.Window('PLC Project', layout)    

    event, values = window.read()    
    window.close()
    
    if(event == None or event == "Exit"):exit()

    function = values['-function-']
    IO = values['-IO-']
    Relay = values['-Relay-']
    if(Relay == "on"):
        Relay = 1
    else:
        Relay = 0

    if function == "read_analog_input":
        result = client.read_analog_input(int(IO))
    elif function == "read_digital_input":
        result = client.read_digital_input(int(IO))
    elif function == "write_digital_output":
        client.write_digital_output(int(IO), int(Relay))
        result = client.read_digital_output(int(IO))
    elif function == "read_digital_output":
        result = client.read_digital_output(int(IO))
    else:
        result = "Invalid function"

    sg.popup('Value of', result)