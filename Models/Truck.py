class Truck: 
    def __init__(self, id: int, brand: str, capacity: int, km_range: int, taken_time_slots=None) -> None:
        self._id = id 
        self._brand = brand 
        self._capacity = capacity
        self._km_range = km_range
        self._taken_time_slots = {} if taken_time_slots is None else taken_time_slots

    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @property
    def capacity(self) -> int:  
        return self._capacity 
    
    @property
    def km_range(self) -> int:
        return self._km_range

    @property
    def taken_time_slots(self):
        return self._taken_time_slots

    def is_time_slot_taken(self, route_id, start_time, end_time):
        for existing_route_id, time_slot in self._taken_time_slots.items():
            if existing_route_id == route_id:
                continue
            if start_time <= time_slot[0] <= end_time or start_time <= time_slot[1] <= end_time:
                return True
        return False

    def update_truck_time_slot(self, route_id, start_time, end_time):
        self._taken_time_slots[route_id] = [start_time, end_time]
    

    def __str__(self):
        return f'Truck information:\n' \
               f'ID: {self._id}\n' \
               f'Brand: {self._brand}\n' \
               f'Capacity: {self._capacity:.2f}kg\n' \
               f'Max range: {self._km_range}km'
    