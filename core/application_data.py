from Models.Customer import *
from Models.Package import *
from Models.Route import *
from Models.Truck import *

class ApplicationData:
    def __init__(self):
        self._trucks = []
        self._packages = []
        self._routes = []

    @property
    def trucks(self):
        return tuple(self._trucks)

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def routes(self):
        return tuple(self._routes)

    def add_truck(self, truck):
        self._trucks.append(truck)

    def add_package(self, package):
        self._packages.append(package)

    def add_route(self, route):
        self._routes.append(route)

    def find_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.id == truck_id:
                return truck
        raise ValueError(f'Truck with id: {truck_id} not found. Try again with a different id!')

    def find_package_by_id(self, package_id):
        for package in self._packages:
            if package.id == package_id:
                return package
        raise ValueError(f'Package with id: {package_id} not found. Try again with a different id!')

    def find_route_by_id(self, route_id):
        for route in self._routes:
            if route.id == route_id:
                return route
        raise ValueError(f'Route with id: {route_id} not found. Try again with a different id!')

    def find_unassigned_packages(self):
        unassigned_packages = [package for package in self._packages if not package._is_assigned]
        return unassigned_packages



