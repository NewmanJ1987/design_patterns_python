from abc import ABC, abstractmethod


class Car:
    def __init__(self, kilometers_since_oil_change, kilometers_since_break_change):
        self.kilometers_since_oil_change = kilometers_since_oil_change
        self.kilometers_since_break_change = kilometers_since_break_change

# Create abstract class to be part for the handler.
class Maintenance(ABC):
    def __init__(self):
        self.next = None

    def set_next(self, maintenance):
        self.next = maintenance

    @abstractmethod
    def get_cost(self, car):
        pass

# Create concrete handler to be part of the chain.
class ChangeOil(Maintenance):
    def get_cost(self, car):
        price = 0
        if car.kilometers_since_oil_change > 5000:
            # do work
            car.kilometers_since_oil_change = 0
            price = 125
        if self.next:
            return price + self.next.get_cost(car)
        return price


# Create concrete handler to be part of the chain.
class ChangeBreak(Maintenance):
    def get_cost(self, car):
        price = 0
        if car.kilometers_since_break_change > 10000:
            # do work
            car.kilometers_since_break_change = 0
            price = 1000
        if self.next:
            return price + self.next.get_cost(car)
        return price


# This is the sender that will send messages to the handler.
class Garage:
    def __init__(self, maintenance):
        self.maintenance = maintenance

    def get_cost(self, car):
        return self.maintenance.get_cost(car)

# Register classes
ABC.register(ChangeOil)
ABC.register(ChangeBreak)

# Example of the chain starting. 
car = Car(6000, 15000)
maintenance = ChangeOil()
maintenance.set_next(ChangeBreak())
garage = Garage(maintenance)

print(garage.get_cost(car))
