from .country import Country
from .device import Device
from .device_type import DeviceType
from .equipment import Equipment
from .material import Matherial
from .sensivity import Sensivity


class DevicesOfElectricityAndMagnetism(Device):
    def __init__(self, price: float, material: Matherial, origin_country: Country,
                 category: Equipment, weight_in_grams: int, device_type: DeviceType, sensivity: Sensivity):
        super().__init__(price, material, origin_country, category, weight_in_grams, device_type)
        self.sensivity = sensivity

    def __del__(self):
        pass

    def __str__(self):
        return super(DevicesOfElectricityAndMagnetism, self).__str__() + f'Sensivity: {self.sensivity.value}\n'

    @property
    def speed(self):
        return self.sensivity
