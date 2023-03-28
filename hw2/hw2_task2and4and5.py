
from abc import ABC
import exceptions

# 2

class Vehicle(ABC):
    # создаем атрибуты со значением по умолчанию
    def __init__(self,weight = 1000, fuel = 50, fuel_consuption = 10):
        self.weight = weight
        self.started = False
        self.fuel_consumption = fuel_consuption

    # start  проверяет, что топлива больше нуля и обновляет состояние started
    def start(self):
        if self.fuel <= 0:
            raise exceptions.LowFuelError("Fuel level is too low to start the vehicle.")
        self.started = True
    # проверяет,
    #   что достаточно топлива для преодоления переданной дистанции,
    #   и изменяет количество оставшегося топлива, иначе выкидывает исключение
    def move(self, distance):
        fuel_required = distance / self.fuel_consumption
        if fuel_required > self.fuel:
            raise exceptions.NotEnoughFuel("Not enough fuel to travel the given distance.")
        self.fuel -= fuel_required

# 4
class Car(Vehicle):
    def set_engine(self, engine):
        self.engine = engine


# 5
class Plane(Vehicle):
    def __init__(self,weight = 1000, fuel = 50, fuel_consumption = 500):
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
