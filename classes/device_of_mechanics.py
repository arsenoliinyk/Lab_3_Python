from .country import Country
from .device import Device
from .device_type import DeviceType
from .equipment import Equipment
from .material import Matherial


class DevicesOfMechanics(Device):
    def __init__(self, price: float, material: Matherial, origin_country: Country,
                 category: Equipment, weight_in_grams: int, device_type: DeviceType, speed: str):
        super().__init__(price, material, origin_country, category, weight_in_grams, device_type)
        self.speed = speed

    def __del__(self):
        pass

    def __str__(self):
        return super(DevicesOfMechanics, self).__str__() + f'Speed: {self.speed}\n'
