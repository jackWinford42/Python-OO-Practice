"""Python serial number generator."""

class SerialGenerator:
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
    def __init__(self, start):
        """Create serial generator for a stating number"""
        self.s = start
        self.orginS = start
    
    def generate(self):
        """Generate the next number in the serial number pattern"""
        returnVal = self.s
        self.s += 1
        return returnVal
    
    def reset(self):
        """Reset the current number to the original number in the serial pattern"""
        self.s = self.orginS