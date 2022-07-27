import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric_car: bool

    def compute_tax(self, electric):
        tax_percentage = 0.05
        if electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo


class VehicleRegistry:

    vehicle_info = { }

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("VW ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def generate_vehicle_id(self, length):
        return ''.join(string.ascii_uppercase, k=length)

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id()
        license_plate = self.generate_vehicle_license()
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()

        vehicle = registry.create_vehicle(brand)



if __name__ == "__main__":
    pass
