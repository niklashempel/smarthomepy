import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_returns_true(self, mock_infrared_sensor: Mock):
        mock_infrared_sensor.return_value = True
        sut = SmartRoom()
        self.assertTrue(sut.check_room_occupancy())

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_returns_false(self, mock_infrared_sensor: Mock):
        mock_infrared_sensor.return_value = False
        sut = SmartRoom()
        self.assertFalse(sut.check_room_occupancy())

    @patch.object(GPIO, "input")
    def test_check_enough_light_returns_true(self, mock_photoresistor: Mock):
        mock_photoresistor.return_value = True
        sut = SmartRoom()
        self.assertTrue(sut.check_enough_light())

    @patch.object(GPIO, "input")
    def test_check_enough_light_returns_false(self, mock_photoresistor: Mock):
        mock_photoresistor.return_value = False
        sut = SmartRoom()
        self.assertFalse(sut.check_enough_light())