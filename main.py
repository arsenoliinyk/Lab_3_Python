from classes.sort_order import SortOrder
from manager.device_manager import DeviceManager
from classes.material import Matherial
from classes.country import Country
from classes.equipment import Equipment
from classes.device_type import DeviceType
from classes.device_of_mechanics import DevicesOfMechanics
from classes.device_of_electricity_and_magnetism import DevicesOfElectricityAndMagnetism
from classes.devices_of_molecular_physics_and_thermodynamics import DevicesOfMolecularPhysicsAndThermodynamics
from classes.devices_of_optics import DevicesOfOptics
from classes.sensivity import Sensivity

if __name__ == '__main__':
    devices = [DevicesOfMechanics(500, "сплав Скло", Country.GERMANY, Equipment.FOR_DEMONSTRATION,
                                  300, DeviceType.MECHANICS, "Not so well"),
               DevicesOfMechanics(3000, "сполука Скло", Country.FRANCE, Equipment.FOR_LABORATORY,
                                  4000, DeviceType.MECHANICS, "Very good"),
               DevicesOfMechanics(1533, "сплав Скло", Country.USA, Equipment.FOR_DEMONSTRATION,
                                  580, DeviceType.MECHANICS, "Good"),
               DevicesOfElectricityAndMagnetism(6000, "сплав Скло", Country.CHINA, Equipment.FOR_LABORATORY,
                                                1500, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.MEDIUM),
               DevicesOfElectricityAndMagnetism(8999, "сплав Скло", Country.CHINA, Equipment.FOR_LABORATORY,
                                                1899, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.LIGHT),
               DevicesOfElectricityAndMagnetism(4999, "сплав Скло", Country.SPAIN, Equipment.FOR_DEMONSTRATION,
                                                300, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.STRONG),
               DevicesOfMolecularPhysicsAndThermodynamics(7000, "сплав Скло", Country.GERMANY,
                                                          Equipment.FOR_DEMONSTRATION,
                                                          8500, DeviceType.MOLECULAR_PHYSICS_AND_THERMODYNAMICS,
                                                          "Enough for demonstrations"),
               DevicesOfMolecularPhysicsAndThermodynamics(10000, "сплав Скло", Country.UKRAINE,
                                                          Equipment.FOR_LABORATORY,
                                                          20000, DeviceType.MOLECULAR_PHYSICS_AND_THERMODYNAMICS,
                                                          "Enough for demonstrations"),
               DevicesOfOptics(200, "сплав Скло", Country.CHINA, Equipment.FOR_DEMONSTRATION,
                               600, DeviceType.OPTICS, "Easy to replace"),
               DevicesOfOptics(700, "сплав Скло", Country.USA, Equipment.FOR_LABORATORY,
                               499, DeviceType.OPTICS, "Hard to replace")]

    manager = DeviceManager(devices)
    print("=========Search Mechanics type of device=========")
    list_of_devices_searched_by_type = manager.search_by_type(DeviceType.MECHANICS)
    for device in list_of_devices_searched_by_type:
        print(device)

    print("=========Sort by price=========")

    list_of_devices_sorted_by_price = manager.sort_by_price(SortOrder.ASC)
    for device in list_of_devices_sorted_by_price:
        print(device)

    print("=========Sort by weight=========")

    list_of_devices_sorted_by_weight = manager.sort_by_weight(SortOrder.DSC)
    for device in list_of_devices_sorted_by_weight:
        print(device)

    print("=========")
