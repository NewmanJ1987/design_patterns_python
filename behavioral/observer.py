from abc import ABC, abstractmethod


# https://www.geeksforgeeks.org/observer-pattern-set-2-implementation/
# Advantage: The subject does not need to know the implentation of its observers it just pushes the data it wants to push
# and the observes are responsible for managing the data.

# Disadvantage: The observers are responsible for unregistering from the subject. This could lead to memory leaks if observer do not explicitly unregister themsevles
# see lapsed listner problem
# https://en.wikipedia.org/wiki/Lapsed_listener_problem
# see weak references.
# https://en.wikipedia.org/wiki/Weak_reference


class Display(ABC):
    # Abstract observer class.
    @abstractmethod
    def update(self, data):
        # This is the method that executes code for the data when it receives new data.
        pass

    @abstractmethod
    def display(self):
        # Method that displays the data could be used in the data.
        pass


class AverageScoreDisplay():
    # Concrete observer class
    def __init__(self):
        super(AverageScoreDisplay, self).__init__()

    def update(self, data):
        pass

    def display(self):
        pass


class CurrentScoreDisplay():
    # Concrete observer class
    def __init__(self):
        super(CurrentScoreDisplay, self).__init__()

    def update(self, data):
        pass

    def display(self):
        pass


class CricketData():
    """
    This is the subject class it must provide a register and an unregister method to add observers
    """
    displays = {
        # Hold Observers
    }
    data = {
        # Hold  Data to send to subjects.
    }

    def register_display(self, display):
        self.displays.update({id(display): id})

    def unregsiter_display(self, display):
        self.displays.pop(id(display))

    def notify_displays(self):
        for id, display in self.displays:
            display.update(self.data)


Display.register(AverageScoreDisplay)
Display.register(CurrentScoreDisplay)
