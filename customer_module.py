from PLC import PLC
import time

client = PLC(plc_name='M172', host='192.168.1.200', port=502)
message = False
for i in range(5):

  print(f'Analog Input 4 is {client.read_analog_input(4)}')
  print(f'Digital Input 1 is {client.read_digital_input(1)}')
  client.write_digital_output(1, 1 if message else 0)
  print(f'Digital output 1 is now {client.read_digital_output(1)}')
  message = not message
  time.sleep(2)
