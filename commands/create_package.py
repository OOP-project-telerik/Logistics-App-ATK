from Models.Customer import Customer
from Models.Package import Package
from commands.base_command import BaseCommand

class CreatePackage(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        start_location = self._params[0]
        end_location = self._params[1]
        weight = self._params[2]
        first_name = self._params[3]
        last_name = self._params[4]
        email = self._params[5]
        phone_number = self._params[6]
        address = self._params[7]

        id = len(self._app_data.packages) + 1
        customer = Customer(first_name, last_name, email, phone_number, address)
        package = Package(id, start_location, end_location, float(weight), customer, False, None)

        self._app_data.add_package(package)
        return f'Package {id} created successfully'