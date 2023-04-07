
from abc import ABC, abstractmethod
from hw2_task1 import *
from hw2_task3 import *

# 2

class Vehicle(ABC):
    # создаем атрибуты со значением по умолчанию
    def __init__(self, weight = 1000, fuel = 50, fuel_consuption = 10):
        self.weight = weight
        self.fuel = fuel
        self.started = False
        self.fuel_consumption = fuel_consuption

    # start  проверяет, что топлива больше нуля и обновляет состояние started
    def start(self):
        if not self.started :
            if self.fuel <= 0:
                raise exceptions.LowFuelError("Fuel level is too low to start the vehicle.")
            self.started = True

    def move(self, distance):
        if not self.started:
            raise exceptions.EngineNotStarted("Engine not started")
        fuel_required = distance / self.fuel_consumption
        if fuel_required > self.fuel:
            raise exceptions.NotEnoughFuel("Not enough fuel to travel the given distance.")
        self.fuel -= fuel_required

# 4
class Car(Vehicle):
    def __init__(self, weight = 1000, fuel = 50, fuel_consumption = 10, engine = None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine if eengine else Engine()
    
    def set_engine(self, engine: Engine) :
        self.engine = engine


# 5
class Plane(Vehicle):
    def __init__(self,weight = 1000, fuel = 50, fuel_consumption = 500, max_cargo = 1000, cargo = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_amount):
        if self.cargo + cargo_amount > self.max_cargo:
            raise exceptions.CargoOverload("Cannot load cargo, weight limit exceeded.")
        else:
            self.cargo += cargo_amount

    def remove_all_cargo(self):
        cargo_value = self.cargo
        self.cargo = 0
        return cargo_value
