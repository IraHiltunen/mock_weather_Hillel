import unittest
from unittest.mock import patch, Mock
import weatherapp


# def function_mock(*args, **kwargs):  # тут треба мабуть координати сталі якісь вертати ?
#     return "ffff"


def coordinates(location):
    # повертає точні координати відносно локації(місто, напр)
    pass


def weather_data(coordinates):
    # повертає дані про погоду відносно координат
    pass


class TestMock(unittest.TestCase):
    # def test_no_mock(self):
    #     weatherapp.get_coordinates("45'26")

    # "weatherapp.get_coordinates" підміняємо функцією function_mock(*args, **kwargs)
    # не робимо запит координат, а одразу підставляємо значення

    # @patch("weatherapp.Name_of_class", MockClass) якщо є класс
    # @patch("weatherapp.get_coordinates", Mock(return_value="get_coordinates"))

    # @patch("weatherapp.get_coordinates", function_mock)
    # def test_with_mock(self):
    #     result = weatherapp.get_coordinates("45'26")
    #     self.assertEqual(result, None)

    @patch("weatherapp.get_weather_data", Mock(return_value="Lviv"))
    # @patch("weatherapp.get_weather_data", coordinates)
    def test_unreal_coordinates(self):
        result = weatherapp.get_weather_data()
        self.assertTrue(result)

    @patch("weatherapp.get_coordinates", Mock(return_value={'lat': 40, 'lon': 10}))
    # @patch("weatherapp.get_coordinates", weather_data)
    def test_unreal_city(self):
        result = weatherapp.get_coordinates()
        self.assertTrue(result)


    #weatherapp.request - мок обʼєкт реквест
    # @patch("weatherapp.request", Mock(return_value="Lviv")

if __name__ == '__main__':
    unittest.main()