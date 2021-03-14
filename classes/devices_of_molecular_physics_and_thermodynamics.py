from .country import Country
from .device import Device
from .device_type import DeviceType
from .equipment import Equipment
from .material import Matherial


class DevicesOfMolecularPhysicsAndThermodynamics(Device):
    def __init__(self, price: float, material: Matherial, origin_country: Country,
                 category: Equipment, weight_in_grams: int, device_type: DeviceType, power: str):
        super().__init__(price, material, origin_country, category, weight_in_grams, device_type)
        self.power = power

    def __del__(self):
        pass

    def __str__(self):
        return super(DevicesOfMolecularPhysicsAndThermodynamics, self).__str__() + f'Power: {self.power}\n'

    @property
    def speed(self):
        return self.power
