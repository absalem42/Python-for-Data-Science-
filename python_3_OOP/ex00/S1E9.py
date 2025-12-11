from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class for characters."""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize character with a first name and alive flag."""
        self.first_name =  first_name
        self.is_alive = is_alive
    
    def die(self):
        """Mark the character as dead (set alive flag to False)."""
        self.is_alive = False



class Stark(Character):
    """Stark family member."""
    def __init__(self, first_name, is_alive=True):
        self.first_name =  first_name
        self.is_alive = is_alive
    def die(self):
        """Set this Stark as dead."""
        self.is__alive = False
