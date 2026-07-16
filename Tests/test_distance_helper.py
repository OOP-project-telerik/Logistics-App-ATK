from helpers.distance_helper import get_distance, get_distances_for_stops
import unittest


class DistanceHelper_Should(unittest.TestCase):
    def test_getDistance_returnsCorrectValue_whenValidLocations(self):
        result = get_distance('SYD', 'MEL')
        self.assertEqual(877, result)

    def test_getDistance_isSymmetric_regardlessOfArgumentOrder(self):
        self.assertEqual(get_distance('SYD', 'MEL'), get_distance('MEL', 'SYD'))

    def test_getDistance_raisesValueError_whenStartLocationInvalid(self):
        with self.assertRaises(ValueError):
            get_distance('XXX', 'SYD')

    def test_getDistance_raisesValueError_whenEndLocationInvalid(self):
        with self.assertRaises(ValueError):
            get_distance('SYD', 'XXX')

    def test_getDistancesForStops_returnsCorrectList_whenMultipleStops(self):
        result = get_distances_for_stops(['BRI', 'SYD', 'MEL'])
        self.assertEqual([909,877], result)

    def test_getDistancesForStops_returnsEmptyList_whenSingleStop(self):
        result = get_distances_for_stops(['SYD'])
        self.assertEqual([], result)
