from commands.base_command import BaseCommand
from core.application_data import ApplicationData
class ShowPackages(BaseCommand):
    def execute(self):
        if not self._app_data.packages:
            raise ValueError("No registered packages")
        return '\n'.join([str(package) for package in self._app_data.packages])