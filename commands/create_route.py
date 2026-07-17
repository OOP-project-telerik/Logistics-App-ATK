from datetime import datetime
from Models.Route import Route
from commands.base_command import BaseCommand
from helpers.distance_helper import get_distances_for_stops
from helpers.validation_helpers import validate_location_code

class CreateRoute(BaseCommand):
    def execute(self):
        departure_time = datetime.fromisoformat(self._params[0])
        stops = self._params[1:]

        if len(stops) < 2:
            raise ValueError('A route must have at least 2 stops')

        stops = [validate_location_code(stop) for stop in stops]
        distances = get_distances_for_stops(stops)
        capacity_per_stop = [0] * len(stops)
        route_id = len(self._app_data.routes) + 1

        route = Route(route_id, distances, None, departure_time, None, capacity_per_stop, stops)
        self._app_data.add_route(route)

        return f'Route {route_id} created successfully'