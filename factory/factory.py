# Factory pattern: Abstract away the creation of an object from the
# client that is creating object.

TWO_WHEEL_VEHICLE = 1
THREE_WHEEL_VEHICLE = 2
FOUR_WHEEL_VEHICLE = 3


class Vehicle():
    def print_vechile(self):
        pass


class TwoWheelVehicle(Vehicle):
    def __init__(self):
        super(TwoWheelVehicle, self).__init__()

    def print_vechile(self):
        print("Two Wheeler")


class FourWheelVehicle(Vehicle):
    def __init__(self):
        super(FourWheelVehicle, self).__init__()

    def print_vechile(self):
        print("Four Wheeler")


class ThreeWheelVehicle(Vehicle):
    def __init__(self):
        super(ThreeWheelVehicle, self).__init__()

    def print_vechile(self):
        print("Three Wheeler")


class VehicleFactory():
    @staticmethod
    def create_vehicle(vehicle_type):
        # For a new vehicle we just modify the factory that is responsible for the creation.
        if vehicle_type == TWO_WHEEL_VEHICLE:
            return TwoWheelVehicle()
        if vehicle_type == THREE_WHEEL_VEHICLE:
            return ThreeWheelVehicle()
        if vehicle_type == FOUR_WHEEL_VEHICLE:
            return FourWheelVehicle()


class Client():
    def __init__(self, vehicle_type):
        # If we add a new vehicle we don't have to modify the code of the client. Which is an advantage when using a factory.
        self.vehicle = VehicleFactory.create_vehicle(vehicle_type)


client = Client(TWO_WHEEL_VEHICLE)
client.vehicle.print_vechile()
