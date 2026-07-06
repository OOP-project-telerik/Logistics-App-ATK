from commands.base_command import BaseCommand

class AssignPackageToRoute(BaseCommand):
    def execute(self):
        package_id = int(self._params[0])
        route_id = int(self._params[1])

        package = self._app_data.find_package_by_id(package_id)
        route = self._app_data.find_route_by_id(route_id)

        new_capacity = route.get_capacity(package.start_location, package.end_location, package.weight)

        if new_capacity is None:
            raise ValueError(f'Route {route.id} does not have enough capacity for package {package.id}')

        package._is_assigned = True
        package._connected_route = route

        return f'Package {package.id} assigned to route {route.id}'