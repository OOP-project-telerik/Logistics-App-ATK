from Models.Truck import Truck
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

def seed_trucks(app_data):
    fleet = [
        ('Scania', 1001, 1010, 42000, 8000),
        ('Man', 1011, 1025, 37000, 10000),
        ('Actros', 1026, 1040, 26000, 13000),
    ]
    for brand, start_id, end_id, capacity, km_range in fleet:
        for truck_id in range(start_id, end_id + 1):
            app_data.add_truck(Truck(truck_id, brand, capacity, km_range))

def main():
    app_data = ApplicationData()
    seed_trucks(app_data)

    factory = CommandFactory(app_data)
    engine = Engine(factory)
    engine.start()

if __name__ == '__main__':
    main()


# show_trucks
# create_package SYD MEL 45 Ivan Ivanov ivan@test.com 0888123456 Sofia Vitosha Street 25
# create_package BRI ADL 3000 Petar Petrov petar@test.com 0899112233 Plovdiv Central Square 1
# show_packages
# show_unassigned_packages
# create_route 2026-10-10T06:00 BRI SYD MEL
# create_route 2026-10-12T06:00 SYD MEL ADL
# show_routes
# find_routes_for_package 1
# assign_truck_to_route 1
# assign_truck_to_route 2
# assign_package_to_route 1 1
# show_package_info 1
# show_unassigned_packages
# show_routes_in_progress
# end