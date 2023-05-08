from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, manufacturer: str, model: str, color: str,
                 year: int, km: int = 0):
        self._year = year
        self._model = model
        self._manufacturer = manufacturer
        self._colors = [color]
        self._km = km

    def get_manufacturer(self):
        return self._manufacturer

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_color(self):
        return self._colors[-1]

    def set_color(self, new_color):
        self._colors.append(new_color)

    def get_original_color(self):
        return self._colors[0]

    def get_km(self):
        return self._km

    @abstractmethod
    def has_enough_resource(self, km):
        pass

    @abstractmethod
    def update_resource(self, km):
        pass

    def drive(self, km):
        if self.has_enough_resource(km):
            self._km += km
            self.update_resource(km)

#from c11.vehicle import Vehicle########################################################################################


class GasolineVehicle(Vehicle):

    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 tank_capacity: int, fuel_consumption: int, fuel_type: str,
                 km: int = 0):

        super().__init__(manufacturer, model, color, year, km)
        self._fuel_type = fuel_type
        self._tank_capacity = tank_capacity
        self._fuel_consumption = fuel_consumption
        self._curr_fuel = 0


    def has_enough_resource(self, km):
        return self._curr_fuel / self._fuel_consumption >= km

    def update_resource(self, km):
        self._curr_fuel -= km / self._fuel_consumption

    def add_fuel(self, liters):
            pass

#from c11.vehicle import Vehicle########################################################################################

class ElectricVehicle(Vehicle):

    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 battery_capacity: int, km_per_kw: int, km: int = 0):
        super().__init__(manufacturer, model, color, year, km)

        self._km_per_kw = km_per_kw
        self._battery_capacity = battery_capacity
        self._current_charge = 0

    def has_enough_resource(self, km):
        return self._current_charge / self._km_per_kw >= km

    def update_resource(self, km):
        self._current_charge -= km / self._km_per_kw

    def charge(self, kw):
        pass

#from c11.electric_vehicle import ElectricVehicle#######################################################################

# if __name__ == '__main__':
#     # v = Vehicle("mazda", "3", "white", 1999)
#     # print(v.get_manufacturer())
#     # print(v._model)
#     # print(v.__dict__)
#     # print(v._Vehicle__manufacturer)
#     ev = ElectricVehicle('tesla', 'model 3', 'white', 2022, 103, 4)
#     ev.drive(100)
#     print("bye")