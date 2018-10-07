# https://en.wikipedia.org/wiki/Decorator_pattern
# Follows the open closed princple open for extension closed for modification.
# We can use a factory with the decorator to control the creation of the object and adding the condiment.
from abc import abstractmethod, ABC


class Drink(ABC):
    # This is the abstract component that deractor and the component both inherit from.
    @abstractmethod
    def get_cost(self):
        pass


class Coffee(Drink):
    # The real component that we decorate.
    def get_cost(self):
        return 1.00


class Condiment(Drink):
    # The abstract obect  that all decorators that we inherit from.
    def __init__(self, drink):
        self.drink = drink


class Cinnamon(Condiment):
    # This is one type of concrete decorator.
    def __init__(self, drink):
        super(Cinnamon, self).__init__(drink)

    def get_cost(self):
        return self.drink.get_cost() + .2


class WhippedCream(Condiment):
    # This is another type of concrete decorator.
    def __init__(self, drink):
        super(WhippedCream, self).__init__(drink)

    def get_cost(self):
        return self.drink.get_cost() + .5


ABC.register(Drink)
drink_1 = WhippedCream(Cinnamon(Coffee()))
