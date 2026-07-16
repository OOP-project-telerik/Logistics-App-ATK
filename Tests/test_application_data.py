from core.application_data import ApplicationData
from Models.Truck import Truck
from Models.Package import Package
from Models.Customer import Customer
from Models.Route import Route
from datetime import datetime, timedelta, time
import unittest

valid_customer = Customer('Test', 'Test', 'test@test.com', '1234567890', '123 Test Street, Test City, Test Country')
default_departure = datetime.combine(datetime.today() + timedelta(1), time(hour=6))


class ApplicationData_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()
        self.truck = Truck(1, 'Scania', 42000, 8000)
        self.package = Package(1, 'BRI', 'SYD', 50, valid_customer, False, None)
        self.route = Route(1, [909], 0, default_departure, self.truck, [], ['BRI', 'SYD'])

    def test_trucksPackagesRoutes_areEmpty_whenNewlyCreated(self):
        self.assertEqual((), self.app_data.trucks)
        self.assertEqual((), self.app_data.packages)
        self.assertEqual((), self.app_data.routes)

    def test_addTruck_addsTruckToTrucksCollection(self):
        self.app_data.add_truck(self.truck)
        self.assertIn(self.truck, self.app_data.trucks)

    def test_addPackage_addsPackageToPackagesCollection(self):
        self.app_data.add_package(self.package)
        self.assertIn(self.package, self.app_data.packages)

    def test_addRoute_addsRouteToRoutesCollection(self):
        self.app_data.add_route(self.route)
        self.assertIn(self.route, self.app_data.routes)

    def test_findTruckById_returnsCorrectTruck_whenExists(self):
        self.app_data.add_truck(self.truck)
        self.assertEqual(self.truck, self.app_data.find_truck_by_id(1))

    def test_findTruckById_raisesValueError_whenNotFound(self):
        with self.assertRaises(ValueError):
            self.app_data.find_truck_by_id(999)

    def test_findUnassignedPackages_returnsOnlyUnassignedOnes(self):
        assigned_package = Package(2, 'BRI', 'SYD', 50, valid_customer, True, None)
        self.app_data.add_package(self.package)
        self.app_data.add_package(assigned_package)

        result = self.app_data.find_unassigned_packages()

        self.assertIn(self.package, result)
        self.assertNotIn(assigned_package, result)

    def test_findRoutesForPackage_returnsMatchingRoute_whenStopsInOrder(self):
        self.app_data.add_route(self.route)
        result = self.app_data.find_routes_for_package(self.package)
        self.assertIn(self.route, result) 

    def test_findRoutesForPackage_excludesRoute_whenStopOrderIsReversed(self):
        reversed_route = Route(2, [909], 0, default_departure, self.truck, [], ['SYD', 'BRI'])
        self.app_data.add_route(reversed_route)

        result = self. app_data.find_routes_for_package(self.package)
        self.assertNotIn(reversed_route, result)

    def test_findFreeTruck_returnsTruck_whenRangeAndCapacitySufficient(self):
        self.app_data.add_truck(self.truck)
        self.assertEqual(self.truck, self.app_data.find_free_truck(self.route))

    def test_findFreeTruck_returnsNone_whenNoTruckHasEnoughRange(self):
        weak_truck = Truck(2, 'Man', 37000, 100)
        self.app_data.add_truck(weak_truck)
        self.assertIsNone(self.app_data.find_free_truck(self.route))

    def test_findFreeTruck_returnsNone_whenTruckAlreadyUsedOnAnotherRoute(self):
        self.app_data.add_truck(self.truck)
        self.app_data.add_route(self.route)
        self.assertIsNone(self.app_data.find_free_truck(self.route))

    def test_findPackageById_returnsCorrectPackage_whenExists(self):
        self.app_data.add_package(self.package)
        self.assertEqual(self.package, self.app_data.find_package_by_id(1))
    
    def test_findPackageById_raisesValueError_whenNotFound(self):
        with self.assertRaises(ValueError):
            self.app_data.find_package_by_id(999)

    def test_findRouteById_returnsCorrectRoute_whenExists(self):
        self.app_data.add_route(self.route)
        self.assertEqual(self.route, self.app_data.find_route_by_id(1))

    def test_findRouteById_raisesValueError_whenNotFound(self):
        with self.assertRaises(ValueError):
            self.app_data.find_route_by_id(999)



