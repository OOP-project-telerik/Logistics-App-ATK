from Models.Customer import Customer 

class Package: 
    def __init__(self, id, start_location, end_location, weight: float, customer: Customer, is_assigned, connected_route):
        self._id = id 

        if len(start_location) != 3:
          raise ValueError(f'Start location must be precisely 3 letters')
        self._start_location = start_location
       
        if len(end_location) != 3:
            raise ValueError(f'End location must be precisely 3 letters')
        self._end_location = end_location
       
        if float(weight) > 42000:
            raise ValueError(f'Weight exceeds maximum limit of 42000 kg')
        if float(weight) <= 0:
            raise ValueError(f'Weight must be a positive number')
        self._weight = weight
    
        self._customer = customer
        self._is_assigned = is_assigned
        self._connected_route = connected_route

    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self): 
        return self._start_location
    
    @property 
    def end_location(self):
        return self._end_location
    
    @property
    def weight(self):
        return self._weight
    
    def __str__(self):
        customer_info = str(self._customer).replace('\n', '\n   ')
        return (f'---Package info:\n---' \
                f'ID: {self.id}\n' \
                f'Start Location: {self.start_location}\n' \
                f'End Location: {self.end_location}\n' \
                f'Weight: {self.weight} kg\n' \
                f'---Customer info:\n---   ' \
                f'Customer: {customer_info}')
