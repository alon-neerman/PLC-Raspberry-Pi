
from M172.Client import Client as M172Client

class PLC(object):
  def __init__(self, plc_name, host, port, require_setup=False):
    if plc_name == 'M172':
      self.client = M172Client(host, port)
  
  def read_analog_input(self, num):
    return self.client.read_analog_input(num)
  
  def read_digital_input(self, num):
    return self.client.read_digital_input(num)
  
  def write_digital_output(self, num, value):
    self.client.write_digital_output(num, value)

  def read_digital_output(self, num):
    return self.client.read_digital_output(num)
