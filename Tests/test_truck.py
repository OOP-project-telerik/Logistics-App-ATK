from Models.Truck import Truck
import unittest


valid_id = 1
valid_brand = 'Scania'
valid_capacity = 42000
valid_km_range = 8000
valid_taken_time_slots = None


class Truck_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        truck = Truck(valid_id, valid_brand, valid_capacity, valid_km_range, valid_taken_time_slots)

        self.assertEqual(valid_id, truck.id)
        self.assertEqual(valid_brand, truck.brand)
        self.assertEqual(valid_capacity, truck.capacity)
        self.assertEqual(valid_km_range, truck.km_range)

        self.assertEqual({}, truck.taken_time_slots)

    def test_properties_whenTryToChange(self):
        truck = Truck(valid_id, valid_brand, valid_capacity, valid_km_range, valid_taken_time_slots)

        with self.assertRaises(AttributeError):
            truck.id = 2
            truck.brand = 'Test'
            truck.capacity = 45
            truck.km_range = 3000

    def test_strMethod_whenCorrect(self):
        truck = Truck(valid_id, valid_brand, valid_capacity, valid_km_range, valid_taken_time_slots)
        valid_str = f'Truck information:\n' \
                    f'ID: 1\n' \
                    f'Brand: Scania\n' \
                    f'Capacity: 42000.00kg\n' \
                    f'Max range: 8000km'

        self.assertEqual(valid_str, str(truck))

    def test_is_time_slot_taken_returnFalseWhenTakenTimeSlotsAttributeIsNone(self):
        truck = Truck(valid_id, valid_brand, valid_capacity, valid_km_range, valid_taken_time_slots)

        func = truck.is_time_slot_taken(1, 4, 5)

        self.assertEqual(False, func)