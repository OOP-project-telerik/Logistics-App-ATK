from Models.Route import Route
from Models.Package import Package
from Models.Truck import Truck
from datetime import datetime, timedelta, time
import unittest 

default_departute_datetime = datetime.combine(datetime.today() + timedelta(1), time(hour=6))
valid_id = 1
valid_distances = [909, 877]
valid_timedelta = 0
valid_truck = Truck(1, 'Scania', 42000, 8000)
valid_capacity_per_stop = []
valid_stops = ['BRI', 'SYD', 'MEL']


class Route_Should(unittest.TestCase):
    def setUp(self):
        self.route = Route(valid_id, valid_distances.copy(), valid_timedelta, default_departute_datetime,
                            valid_truck, valid_capacity_per_stop.copy(), valid_stops.copy())

    def test_initializerWithCorrectInput(self):
        self.assertEqual(valid_id, self.route.id)
        self.assertEqual(valid_distances, self.route.distances)
        self.assertEqual(default_departute_datetime, self.route.departure_time)
        self.assertEqual(valid_truck, self.route.truck)
        self.assertEqual(valid_capacity_per_stop, self.route.delivery_weight_per_stop)
        self.assertEqual(valid_stops, self.route.stops)

    def test_totalDistancesProperty_returnZeroWhenSumEmptyList(self):
        self.assertEqual(sum(valid_distances), self.route.total_distance)

    def test_arrivalTimeProperty_returnDefaultDepartureTimeAtSixOClockTommorow(self):
        time_to_travel_in_mins = int((self.route.total_distance / Route.DEFAULT_SPEED) * 60)
        result = self.route.departure_time + timedelta(minutes=time_to_travel_in_mins)

        self.assertEqual(str(result), str(self.route.arrival_time))
        self.assertEqual(result, self.route.arrival_time)

    def test_findArrivalTimesFunction_whenDefaultDepartureTime(self):
        result = self.route.find_arrival_times()

        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], datetime)
        self.assertEqual(result, self.route.find_arrival_times())

    def test_getArrivalTimeForStopFunction_whenParamsAreValid_(self):
        arrival_time_for_stop = self.route.get_arrival_time_for_stop('MEL')
        result_str = arrival_time_for_stop

        self.assertIsInstance(result_str, str)
        self.assertEqual(result_str, str(arrival_time_for_stop))

    def test_getCapacityFunction_whenEnoughRouteCapacity(self):
        self.assertEqual([41950, 41950, 41950], self.route.get_capacity('BRI', 'SYD', 50))

    def test_getCapacityFunction_returnNoneWhenNotEnoughRouteCapacity(self):
        self.assertEqual(None, self.route.get_capacity('BRI', 'MEL', 45000))

    def test_getNextStopFunction_whenParamsAreValid(self):
        result = self.route.get_next_stop()

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], str)
        self.assertIsInstance(result[1], datetime)

    def test_getNextStopFunction_returnValueError_whenStartLocationIsNone(self):
        self.route.stops = []
        self.route.distances = []
        with self.assertRaises(ValueError):
            self.route.get_next_stop()

    def test_removeStopFunction(self):
        self.route.remove_stop()

        self.assertEqual([909], self.route.distances)
        self.assertEqual(['BRI', 'SYD'], self.route.stops)

    def test_findNextStopAndArrivalTimeFunction(self):
        slots = self.route.find_arrival_times()
        result = self.route.find_next_stop_and_arrival_time(datetime.now(), slots)

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], str)
        self.assertIsInstance(result[1], datetime)

    def test_strMethod(self):
        self.assertEqual('ID: [1] ', str(self.route))
