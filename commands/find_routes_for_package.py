from commands.base_command import BaseCommand

class FindRoutesForPackage(BaseCommand):
    def execute(self):
        package_id = int(self._params[0])
        package = self._app_data.find_package_by_id(package_id)
        routes = self._app_data.find_routes_for_package(package)
        if not routes:
            raise ValueError(f'No suitable routes found for package {package.id}')
        return '\n'.join([str(route) for route in routes])