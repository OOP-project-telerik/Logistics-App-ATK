class Truck: 
    def __init__(self, id: int, brand: str, capacity: int, km_range: int):
        self._id = id 
        self._brand = brand 
        self._capacity = capacity
        self._km_range = km_range
    
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
    