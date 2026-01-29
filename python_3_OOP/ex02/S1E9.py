from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize character with a first name and alive flag."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark family member."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Mark this Stark as dead."""
        self.is_alive = False
