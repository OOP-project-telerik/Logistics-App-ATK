from Models.Truck import Truck
from datetime import datetime, timedelta, time 

def add_days_to_now(d):
    return datetime.combine(datetime.now().date() + timedelta(d + 1), time(hour=6))

class Route:
    default_dep_time = datetime.combine(datetime.now().date() + timedelta(1), time(hour=6))
    DEFAULT_SPEED = 87 
    
    def __init__(self, id: int, distance: list, time_delta, departure_time, truck, capacity_per_stop,stops):
        self.id = id 
        self.distances = distance 

        if departure_time:
            self.departure_time = departure_time
        else:
            if time_delta:
                self.departure_time = Route.default_dep_time
            else:
                self.departure_time = add_days_to_now(time_delta)
        self.stops = stops 
        self.truck = truck 
        self.delivery_weight_per_stop = capacity_per_stop 

    @property
    def total_distance(self):
        return sum(self.distances) 
    
    @property 
    def arrival_time(self):
        time_to_travel_min = int((self.total_distance / Route.DEFAULT_SPEED) * 60)
        return self.departure_time + timedelta(minutes = time_to_travel_min)
    
    def find_arrival_times(self): 
        time_slot = [self.departure_time]
        current_slot = self.departure_time

        for d in self.distances: 
            total_time_distance_min = int((d / Route.DEFAULT_SPEED) * 60) 
            arrival_time = current_slot + timedelta(minutes = total_time_distance_min)
            time_slot.append(arrival_time)
            current_slot = arrival_time

        return time_slot

    def get_arrival_time_for_stop(self, stop: str):
        if stop not in self.stops:
            return None  
        idx = self.stops.index(stop)
        return self.custom_strftime("%b {S} %H:%Mh", self.find_arrival_times()[idx])

    def get_capacity(self, start_location: str, end_location: str, package_weight):
        start_index = self.stops.index(start_location)
        end_index = self.stops.index(end_location)
        
        route_capacity = [
        self.truck.capacity - c for c in self.delivery_weight_per_stop
        ] if sum(self.delivery_weight_per_stop) != 0 else [self.truck.capacity] * len(self.stops) 
        
        enough_capacity = not any(
        
        package_weight > route_capacity[i] for i in range(start_index, len(self.stops)))
        if not enough_capacity:
            return None 
        
        route_capacity = [
        r - package_weight if i >= start_index else r
        for i, r in enumerate(route_capacity)]
        
        self.delivery_weight_per_stop = [
        w + package_weight if i >= start_index else w
        for i, w in enumerate(self.delivery_weight_per_stop)] 

        return route_capacity 
    
    def get_next_stop(self):
        if not self.stops:
            raise ValueError('No stops available on this route')
        slots = self.find_arrival_times()
        return self.find_next_stop_and_arrival_time(datetime.now(), slots)

    def remove_stop(self):
        self.stops.pop()
        self.distances.pop()

    @staticmethod
    def custom_strftime(format_string: str, t) -> str:
        d = t.day
        suffix = 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
        return t.strftime(format_string).replace('{S}', str(d) + suffix) 
    
    def find_next_stop_and_arrival_time(self, datetime_now, slots):
        for stop, slot in zip(self.stops, slots):
            if slot >= datetime_now:
             return stop, slot
        return self.stops[-1], slots[-1] 
    
    def __str__(self) -> str:
        route_id = f'ID: [{self.id}] '
        result = [f'{x} ({self.custom_strftime("%b {S} %H:%Mh", y)} delivery weight: {z}kg)'
        for x, y, z in zip(self.stops, self.find_arrival_times(), self.delivery_weight_per_stop)]
        
        return route_id + ' → '.join(result)
