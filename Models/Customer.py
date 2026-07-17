class Customer: 

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, address: str):
        
        if len(first_name) < 2 or len(first_name) > 15 or not first_name.isalpha():
           raise ValueError(f'!!! ERROR FIRST NAME: "{first_name}"!!!\n'
                             f'   -First name can contain ONLY letters and length has to be 2-15 symbols!') 
        if len(last_name) < 2 or len(last_name) > 15 or not last_name.isalpha():
            raise ValueError(f'!!! ERROR LAST NAME: "{last_name}"!!!\n'
                             f'   -Last name can contain ONLY letters and length has to be 2-15 symbols!')
        if len(email) < 5 or len(email) > 30 or '@' not in email or '.' not in email:
            raise ValueError(f'!!! ERROR EMAIL: "{email}"!!!\n'
                             f'   -Email has to be 5-30 symbols and contain "@" and "." symbols!')
        if len(phone_number) < 10 or len(phone_number) > 15 or not phone_number.isdigit():
            raise ValueError(f'!!! ERROR PHONE NUMBER: "{phone_number}"!!!\n'
                             f'   -Phone number has to be 10-15 digits!')
        if len(address) < 5 or len(address) > 100:
            raise ValueError(f'!!! ERROR ADDRESS: "{address}"!!!\n'
                             f'   -Address has to be 5-100 symbols!')

        self._first_name = first_name.capitalize()
        self._last_name = last_name.capitalize()
        self._email = email
        self._phone_number = phone_number
        self._address = address

    @property 
    def first_name(self):
        return self._first_name
 
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @property
    def address(self):
        return self._address
    
    def __str__(self):
        return (
        f'Customer: {self.first_name} {self.last_name}\n'
        f'Email: {self.email}\n'
        f'Phone: {self.phone_number}\n'
        f'Address: {self.address}')
