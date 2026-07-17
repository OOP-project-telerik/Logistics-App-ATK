from core.application_data import ApplicationData
from commands.create_package import CreatePackage
from commands.create_route import CreateRoute
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.assign_package_to_route import AssignPackageToRoute
from commands.find_routes_for_package import FindRoutesForPackage
from commands.show_packages import ShowPackages
from commands.show_routes import ShowRoutes
from commands.show_trucks import ShowTrucks
from commands.show_unassigned_packages import ShowUnassignedPackages
from commands.show_package_info import ShowPackageInfo
from commands.show_routes_in_progress import ShowRoutesInProgress

class CommandFactory:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data
        self._commands = {
            'create_package': CreatePackage,
            'create_route': CreateRoute,
            'assign_truck_to_route': AssignTruckToRoute,
            'assign_package_to_route': AssignPackageToRoute,
            'find_routes_for_package': FindRoutesForPackage,
            'show_packages': ShowPackages,
            'show_routes': ShowRoutes,
            'show_trucks': ShowTrucks,
            'show_unassigned_packages': ShowUnassignedPackages,
            'show_package_info': ShowPackageInfo,
            'show_routes_in_progress': ShowRoutesInProgress,
        }

    def create(self, cmd_name, params):
        cmd_name = cmd_name.lower()
        if cmd_name not in self._commands:
            raise ValueError(f"Invalid command '{cmd_name}'")
        command_class = self._commands[cmd_name]
        return command_class(params, self._app_data)