from commands.base_command import BaseCommand
class ShowUnassignedPackages(BaseCommand):
    def execute(self):
        if not self._app_data.find_unassigned_packages():
            raise ValueError("All packages are assigned!")
        return '\n'.join([str(package) for package in self._app_data.find_unassigned_packages()])
