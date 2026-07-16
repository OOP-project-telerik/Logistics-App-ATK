from commands.base_command import BaseCommand
from helpers.time_helper import is_in_progress


class ShowRoutesInProgress(BaseCommand):
    def execute(self):
        routes_in_progress = [ 
            route for route in self._app_data.routes 
            if is_in_progress(route.departure_time, route.arrival_time)
        ]

        if not routes_in_progress:
            raise ValueError(f"No routes are currently in progress")
        
        return '\n'.join([str(route) for route in routes_in_progress])