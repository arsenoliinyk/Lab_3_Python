from classes.country import Country
from classes.equipment import Equipment
from classes.device_type import DeviceType
from classes.material import Matherial


class Device:
    def __init__(self, price: float, material: Matherial, origin_country: Country,
                 category: Equipment, weight_in_grams: int, device_type: DeviceType):
        self.price = price
        self.material = material
        self.origin_country = origin_country
        self.category = category
        self.weight_in_grams = weight_in_grams
        self.device_type = device_type

    def __del__(self):
        pass

    def __str__(self):
        return f'Price: {self.price}\n' \
               f'Material: {self.material}\n' \
               f'Origin country: {self.origin_country}\n' \
               f'Category: {self.category}\n' \
               f'Weight in grams: {self.weight_in_grams}\n' \
               f'Type: {self.device_type.value}\n'
