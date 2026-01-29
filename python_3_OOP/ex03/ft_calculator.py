class calculator:
    """
    A calculator class that performs vector operations.
    
    Takes a vector (list of int/float) and performs
    operations with a scalar value on all elements.
    """

    def __init__(self, vector):
        """
        Initialize calculator with a vector.
        
        Args:
            vector (list): A list of int/float values.
        """
        self.vector = vector

    def __add__(self, scalar):
        """Add scalar to all elements and print result."""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar):
        """Multiply all elements by scalar and print result."""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar):
        """Subtract scalar from all elements and print result."""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar):
        """
        Divide all elements by scalar and print result.
        
        Raises:
            ZeroDivisionError: If scalar is 0.
        """
        if scalar == 0:
            print("Error: Division by zero.")
            return
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
