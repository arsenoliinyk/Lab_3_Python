from audioop import reverse

from classes.device import Device
from classes.device_type import DeviceType
from classes.sort_order import SortOrder


class DeviceManager:
    def __init__(self, devices=[]):
        self.devices = devices

    def __del__(self):
        pass

    def search_by_type(self, type_of_device: DeviceType):
        search_type = []
        for device in self.devices:
            if device.device_type == type_of_device:
                search_type.append(device)
        return search_type

    def sort_by_price(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.devices, key=lambda device: device.price, reverse=False)
        return sorted(self.devices, key=lambda device: device.price, reverse=True)

    def sort_by_weight(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.devices, key=lambda device: device.weight_in_grams, reverse=False)
        return sorted(self.devices, key=lambda device: device.weight_in_grams, reverse=True)
