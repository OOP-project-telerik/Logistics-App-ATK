from commands.base_command import BaseCommand
class ShowTrucks(BaseCommand):
    def execute(self):
        if not self._app_data.trucks:
            raise ValueError("No registered trucks")
        return '\n'.join([str(truck) for truck in self._app_data.trucks])