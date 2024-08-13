import unittest
from unittest.mock import patch, Mock
import weatherapp


def coordinates(location):
    # повертає точні координати відносно локації(місто, напр)
    pass


def weather_data(coordinates):
    # повертає дані про погоду відносно координат
    pass

class MockResponse:
    def json(self):
        return [{"lat": 1, "lon": 1}]

    def raise_for_status(self):
        pass

class MockWeatherResponse:
    def json(self):
        return {
            'current':{
                'temp': 20,
                'wind_speed': 5,
                'rain': {'1h': 0.1}
            }
        }

    def raise_for_status(self):
        pass

class TestMock(unittest.TestCase):

    @patch("weatherapp.requests.get", Mock(return_value=MockResponse()))
    def test_weather_data(self):
        result = weatherapp.get_coordinates("jhkjhkjsh")
        self.assertDictEqual(result, {"lat": 1, "lon": 1})

    # @patch("weatherapp.get_weather_data", Mock(return_value=MockWeatherResponse()))
    @patch("weatherapp.requests.get", Mock(return_value=MockWeatherResponse()))
    def test_weather_data2(self):
        coordinates = {"lat": 1, "lon": 1}
        result = weatherapp.get_weather_data(coordinates)
        expected_result = {'latitude': 1,
                            'longitude': 1,
                            'temperature': 20,
                            'wind_speed': 5,
                            'precipitation': 0.1,
                            'location': "Lat: 1, Lon: 1"}
        self.assertDictEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()