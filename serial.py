"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start):
        """this function initializes the serial generator and set the current number to the start number provided"""
        self.start = start
        self.current_num = start
        
    
    def generate(self):
        """this function increments the number and returns the number"""
        serial_number = self.current_num
        self.current_num += 1
        return serial_number
    
    def reset(self):
        """this resets the current number to the initial number passed in"""
        self.current_num = self.start

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

