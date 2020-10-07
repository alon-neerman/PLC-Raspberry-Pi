
from pyModbusTCP.client import ModbusClient
from IO import IO

class Client(object):
  def __init__(self, host, port, requires_setup=False):
    if requires_setup:
      self.setup_client()
    self.client = ModbusClient()
    self.client.host(host)
    self.client.port(port)
    if not self.client.is_open():
      if not self.client.open():
        raise Exception(f'Unable to connect to server {HOST}:{PORT}')
    self.ANALOG_IN = [IO(self.client, num + 1, 8335 + num) for num in range(8)]
    self.ANALOG_OUT = [IO(self.client, num + 1, 8447 + num) for num in range(2)]
    self.DIGITAL_IN = [IO(self.client, num + 1, 8191 + num) for num in range(2)]
    self.DIGITAL_OUT = [IO(self.client, num + 1, 8527 + num) for num in range(6)]
  

  def setup_client(self):
    return
    
  
  def read_analog_input(self, num):
    if num >= len(self.ANALOG_IN):
      raise Exception('Analog input out of range')
    io = [x for x in self.ANALOG_IN if x.num == num][0]
    return io.find_value() / 100
  

  def read_digital_input(self, num):
    if num >= len(self.DIGITAL_IN):
      raise Exception('Digital input out of range')
    io = [x for x in self.DIGITAL_IN if x.num == num][0]
    return bool(io.find_value())
  

  def write_digital_output(self, num, value):
    if num >= len(self.DIGITAL_OUT):
      raise Exception('Digital output out of range')
    io = [x for x in self.DIGITAL_OUT if x.num == num][0]
    io.write_value(value)

  def read_digital_output(self, num):
    if num >= len(self.DIGITAL_OUT):
      raise Exception('Digital output out of range')
    io = [x for x in self.DIGITAL_OUT if x.num == num][0]
    return bool(io.find_value())


