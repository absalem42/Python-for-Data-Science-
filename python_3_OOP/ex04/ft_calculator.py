class calculator:
    """
    A static calculator class for vector operations.
    
    Performs element-wise operations between two vectors
    using static methods (no instance required).
    """

    @staticmethod
    def dotproduct(V1, V2):
        """
        Calculate and print the dot product of two vectors.
        
        Args:
            V1 (list): First vector.
            V2 (list): Second vector.
        """
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1, V2):
        """
        Add two vectors element-wise and print result.
        
        Args:
            V1 (list): First vector.
            V2 (list): Second vector.
        """
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1, V2):
        """
        Subtract V2 from V1 element-wise and print result.
        
        Args:
            V1 (list): First vector.
            V2 (list): Second vector.
        """
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
