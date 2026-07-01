from commands.base_command import BaseCommand
class ShowRoutes(BaseCommand):
    def execute(self):
        if not self._app_data.routes:
            raise ValueError("No registered routes")
        return '\n'.join([str(route) for route in self._app_data.routes])