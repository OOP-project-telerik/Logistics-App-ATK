from commands.base_command import BaseCommand

class ShowPackageInfo(BaseCommand):
    def execute(self):
        package_id = int(self._params[0])
        package = self._app_data.find_package_by_id(package_id)
        return str(package)