import unittest

from classes.sort_order import SortOrder
from manager.device_manager import DeviceManager
from classes.country import Country
from classes.equipment import Equipment
from classes.device_type import DeviceType
from classes.device_of_mechanics import DevicesOfMechanics
from classes.device_of_electricity_and_magnetism import DevicesOfElectricityAndMagnetism
from classes.devices_of_molecular_physics_and_thermodynamics import DevicesOfMolecularPhysicsAndThermodynamics
from classes.devices_of_optics import DevicesOfOptics
from classes.sensivity import Sensivity


class TestShopManager(unittest.TestCase):

    def setUp(self):
        self.d1 = DevicesOfMechanics(500, "сплав Скло", Country.GERMANY, Equipment.FOR_DEMONSTRATION,
                                     300, DeviceType.MECHANICS, "Not so well")
        self.d2 = DevicesOfMechanics(3000, "сполука Скло", Country.FRANCE, Equipment.FOR_LABORATORY,
                                     4000, DeviceType.MECHANICS, "Very good")
        self.d3 = DevicesOfMechanics(1533, "сплав Скло", Country.USA, Equipment.FOR_DEMONSTRATION,
                                     580, DeviceType.MECHANICS, "Good")
        self.d4 = DevicesOfElectricityAndMagnetism(6000, "сплав Скло", Country.CHINA, Equipment.FOR_LABORATORY,
                                                   1500, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.MEDIUM)
        self.d5 = DevicesOfElectricityAndMagnetism(8999, "сплав Скло", Country.CHINA, Equipment.FOR_LABORATORY,
                                                   1899, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.LIGHT)
        self.d6 = DevicesOfElectricityAndMagnetism(4999, "сплав Скло", Country.SPAIN, Equipment.FOR_DEMONSTRATION,
                                                   600, DeviceType.ELECTRICITY_AND_MAGNETISM, Sensivity.STRONG)
        self.d7 = DevicesOfMolecularPhysicsAndThermodynamics(7000, "сплав Скло", Country.GERMANY,
                                                             Equipment.FOR_DEMONSTRATION,
                                                             8500, DeviceType.MOLECULAR_PHYSICS_AND_THERMODYNAMICS,
                                                             "Enough for demonstrations")
        self.d8 = DevicesOfMolecularPhysicsAndThermodynamics(10000, "сплав Скло", Country.UKRAINE,
                                                             Equipment.FOR_LABORATORY,
                                                             20000, DeviceType.MOLECULAR_PHYSICS_AND_THERMODYNAMICS,
                                                             "Enough for demonstrations")
        self.d9 = DevicesOfOptics(200, "сплав Скло", Country.CHINA, Equipment.FOR_DEMONSTRATION,
                                  800, DeviceType.OPTICS, "Easy to replace")
        self.d10 = DevicesOfOptics(700, "сплав Скло", Country.USA, Equipment.FOR_LABORATORY,
                                   499, DeviceType.OPTICS, "Hard to replace")

        self.deviceManager = DeviceManager(
                                        [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8,
                                         self.d9, self.d10]
        )

    def tearDown(self):
        pass

    def test_search_by_type(self):
        self.assertEqual(
            self.deviceManager.search_by_type(DeviceType.MECHANICS),
            [self.d1, self.d2, self.d3]
        )

    def test_sort_by_price(self):
        self.assertEqual(
            self.deviceManager.sort_by_price(SortOrder.ASC),
            [self.d9, self.d1, self.d10, self.d3, self.d2, self.d6, self.d4, self.d7, self.d5, self.d8]
        )

        self.assertEqual(
            self.deviceManager.sort_by_price(SortOrder.DSC),

            [self.d8, self.d5, self.d7, self.d4, self.d6, self.d2, self.d3, self.d10, self.d1, self.d9]
        )

    def test_sort_by_weight(self):
        self.assertEqual(
            self.deviceManager.sort_by_weight(SortOrder.ASC),
            [self.d1, self.d10, self.d3, self.d6, self.d9, self.d4, self.d5, self.d2, self.d7, self.d8]
        )

        self.assertEqual(
            self.deviceManager.sort_by_weight(SortOrder.DSC),

            [self.d8, self.d7, self.d2, self.d5, self.d4, self.d9, self.d6, self.d3, self.d10, self.d1]
        )


if __name__ == '__main__':
    unittest.main()
