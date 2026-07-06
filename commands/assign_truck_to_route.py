from commands.base_command import BaseCommand

class AssignTruckToRoute(BaseCommand):
    def execute(self):
        route_id = int(self._params[0])
        route = self._app_data.find_route_by_id(route_id)
        truck = self._app_data.find_free_truck(route)

        if truck is None:
            raise ValueError("There are no free trucks")

        route.truck = truck
        return f'Truck {truck.id} assigned to route {route.id}'