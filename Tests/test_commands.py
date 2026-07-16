import unittest
from datetime import datetime, timedelta, time
from core.application_data import ApplicationData
from Models.Truck import Truck
from Models.Package import Package
from Models.Customer import Customer
from Models.Route import Route
from commands.show_unassigned_packages import ShowUnassignedPackages
from commands.show_package_info import ShowPackageInfo
from commands.show_routes_in_progress import ShowRoutesInProgress
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.assign_package_to_route import AssignPackageToRoute

valid_customer = Customer('Test', 'Test', 'test@test.com', '1234567890', '123 Test Street, Test City, Test Country')
default_departure = datetime.combine(datetime.today() + timedelta(1), time(hour=6))


class Commands_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()
        self.truck = Truck(1, 'Scania', 42000, 8000)
        self.package = Package(1, 'BRI', 'SYD', 50, valid_customer, False, None)
        self.route = Route(1, [909], 0, default_departure, self.truck, [], ['BRI', 'SYD'])

    def test_showUnassignedPackages_returnsUnassignedPackages(self):
        self.app_data.add_package(self.package)
        cmd = ShowUnassignedPackages([], self.app_data)
        self.assertIn('BRI', cmd.execute())

    def test_showUnassignedPackages_raiseValueError_whenNoneUnassigned(self):
        cmd = ShowUnassignedPackages([], self.app_data)
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_showPackageInfo_returnsPackageDetails_whenExist(self):
        self.app_data.add_package(self.package)
        cmd = ShowPackageInfo(['1'], self.app_data)
        self.assertIn('BRI', cmd.execute())

    def test_showPackageInfo_raisesValueError_whenNotFound(self):
        cmd = ShowPackageInfo(['999'], self.app_data)
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_showRoutesInProgress_returnsInProgressRoutes(self):
        in_progress_route = Route(2, [909], 0, datetime.now() - timedelta(hours=1), self.truck, [], ['BRI', 'SYD'])
        self.app_data.add_route(in_progress_route)
        cmd = ShowRoutesInProgress([], self.app_data)
        self.assertIn('ID: [2]', cmd.execute())

    def test_showRoutesInProgress_raiseValueError_whenNoneInProgress(self):
        self.app_data.add_route(self.route)
        cmd = ShowRoutesInProgress([], self.app_data)
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_assignTruckToRoute_assignsFreeTruck(self):
        route_without_truck = Route(2, [909], 0, default_departure, None, [], ['BRI', 'SYD'])
        self.app_data.add_truck(self.truck)
        self.app_data.add_route(route_without_truck)
        cmd = AssignTruckToRoute(['2'], self.app_data)
        cmd.execute()
        self.assertEqual(self.truck, route_without_truck.truck)

    def test_assigntruckToRoute_raisesValueError_whenNoFreeTruck(self):
        self.app_data.add_route(self.route)
        cmd = AssignTruckToRoute(['1'], self.app_data)
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_assignPackageToRoute_assignsPackage_whenCapacitySufficient(self):
        self.app_data.add_package(self.package)
        self.app_data.add_route(self.route)
        cmd = AssignPackageToRoute(['1', '1'], self.app_data)
        cmd.execute()
        self.assertTrue(self.package.is_assigned)

    def test_assignPackageToRoute_raiseValueError_WhenNotEnoughCapacity(self):
        low_capacity_truck = Truck(3, 'Man', 40, 8000)
        low_capacity_route = Route(3, [909], 0, default_departure, low_capacity_truck, [], ['BRI', 'SYD'])
        heavy_package = Package(3, 'BRI', 'SYD', 50, valid_customer, False, None)
        self.app_data.add_package(heavy_package)
        self.app_data.add_route(low_capacity_route)
        cmd = AssignPackageToRoute(['3', '3'], self.app_data)
        with self.assertRaises(ValueError):
            cmd.execute()

