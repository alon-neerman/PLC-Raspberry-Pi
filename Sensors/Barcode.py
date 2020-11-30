from usb_scanner.scanner import barcode_reader

# This class is responsible for handling the Barcode scanner input
# it uses this library: https://github.com/julzhk/usb_barcode_scanner
class Barcord:
    def __init__(self): 
        #shoudn't need to do anything here

    #Fetches the reading on the barcode scanner
    def getReading(self):
        upcnumber = ''
        try:    
            #read until we get an input
            #todo: do we want a timeout of some sort?
            while(upcnumber == '')
                upcnumber = barcode_reader()
            return upcnumber
        except Exception as e:
            return "Error getting reading"    
