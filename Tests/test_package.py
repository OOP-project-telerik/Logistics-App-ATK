from Models.Package import Package
from Models.Customer import Customer
import unittest

valid_id = 1
valid_start_location = 'BRI'
valid_end_location = 'MEL'
valid_weight = 45.5
valid_customer_info = Customer('Test', 'Test', 'test@test.com', '1234567890', '123 Test Street, Test City, Test Country')
valid_is_assigned = True
valid_connected_route = 1


class Package_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        package = Package(valid_id, valid_start_location, valid_end_location, valid_weight, valid_customer_info,
                          valid_is_assigned, valid_connected_route)

        self.assertEqual(valid_id, package._id)
        self.assertEqual(valid_start_location, package._start_location)
        self.assertEqual(valid_end_location, package._end_location)
        self.assertEqual(valid_weight, package._weight)

        self.assertEqual(valid_customer_info, package.customer_info)  # customer_info should be Customer object

        # check types of is_assigned and connected_route
        self.assertEqual(bool, type(package.is_assigned))  # is_assigned should be bool
        self.assertEqual(int, type(package.connected_route))  # connected_route should be int

        self.assertEqual(float, type(package.weight))  # check if type of weight is float

    def test_initializerWithIncorrectInput(self):
        # start_location should be exactly 3 symbols

        with self.assertRaises(ValueError):  # start_location is not exactly 3 symbols
            Package(valid_id, 'Test', valid_end_location, valid_weight, valid_customer_info,
                    valid_is_assigned, valid_connected_route)
        # end_location should be exactly 3 symbols

        with self.assertRaises(ValueError):  # end_location is not exactly 3 symbols
            Package(valid_id, valid_start_location, 'Test', valid_weight, valid_customer_info,
                    valid_is_assigned, valid_connected_route)
        # weight should be type float, from 0 to 42 000 kilograms
        with self.assertRaises(ValueError):  # weight is 43 000 kg
            Package(valid_id, valid_start_location, valid_end_location, 43000, valid_customer_info,
                    valid_is_assigned, valid_connected_route)
        with self.assertRaises(ValueError):  # weight is 43 000 kg
            Package(valid_id, valid_start_location, valid_end_location, -500, valid_customer_info,
                    valid_is_assigned, valid_connected_route)

    def test_properties_whenTryToChange(self):
        package = Package(valid_id, valid_start_location, valid_end_location, valid_weight, valid_customer_info,
                          valid_is_assigned, valid_connected_route)

        with self.assertRaises(AttributeError):
            package.id = 2
        with self.assertRaises(AttributeError):
            package.start_location = 'Mel'
        with self.assertRaises(AttributeError):
            package.end_location = 'Bri'
        with self.assertRaises(AttributeError):
            package.weight = 10.500

    def test_strMethod_whenCorrect(self):
        package = Package(valid_id, valid_start_location, valid_end_location, valid_weight, valid_customer_info,
                          valid_is_assigned, valid_connected_route)

        customer_info_str = str(package.customer_info).replace('\n', '\n    ')

        valid_str = f'---Package info: ---\n' \
                    f'   #Package ID: [1]\n' \
                    f'   #Package start location: BRI\n' \
                    f'   #Package end location: MEL\n' \
                    f'   #Package weight: 45.5kg\n' \
                    f'   ---Customer info: ---\n' \
                    f'      {customer_info_str}'

        self.assertEqual(valid_str, str(package))