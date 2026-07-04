from Models.Customer import Customer
import unittest

valid_first_name = 'Test'
valid_last_name = 'Test'
valid_email = 'test@test.com'
valid_phone_number = '1234567890'
valid_address = '123 Test Street, Test City, Test Country'



class Customer_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        customer = Customer(valid_first_name, valid_last_name, valid_email, valid_phone_number, valid_address)
        self.assertEqual(valid_first_name, customer._first_name)
        self.assertEqual(valid_last_name, customer._last_name)
        self.assertEqual(valid_email, customer._email)
        self.assertEqual(valid_phone_number, customer._phone_number)
        self.assertEqual(valid_address, customer._address)

    def test_properties_whenTryToChange(self):
        customer = Customer(valid_first_name, valid_last_name, valid_email, valid_phone_number, valid_address)

        with self.assertRaises(AttributeError):
            customer.first_name = 'Test'
        with self.assertRaises(AttributeError):
            customer.last_name = 'Test'
        with self.assertRaises(AttributeError):
            customer.email = 'Test@abv.bg'
        with self.assertRaises(AttributeError):
            customer.phone_number = '0987654321'
        with self.assertRaises(AttributeError):
            customer.address = '456 Test Avenue, Test City, Test Country'

    def test_initializerWithIncorrectInput(self):
        # first_name should be from 2 to 15 characters
        with self.assertRaises(ValueError):  # first_name less than 2 characters
            Customer('T', valid_last_name, valid_email, valid_phone_number, valid_address)
        with self.assertRaises(ValueError):  # first_name more than 15 characters
            Customer('Testtesttesttesttest', valid_last_name, valid_email, valid_phone_number, valid_address)                   
        # last_name should be from 2 to 15 characters
        with self.assertRaises(ValueError):  # last_name less than 2 characters
            Customer(valid_first_name, 'T', valid_email, valid_phone_number, valid_address)
        with self.assertRaises(ValueError):  # last_name more than 15 characters
            Customer(valid_first_name, 'Testtesttesttesttest', valid_email, valid_phone_number, valid_address)
        # email should be from 5 to 30 characters and should contain '@' and '.' symbols
        with self.assertRaises(ValueError):  # email less than 5 characters
            Customer(valid_first_name, valid_last_name, '@.bg', valid_phone_number, valid_address)
        with self.assertRaises(ValueError):  # email more than 30 characters
            Customer(valid_first_name, valid_last_name, 'testtesttesttesttesttestesttest@.bg', valid_phone_number, valid_address)
        with self.assertRaises(ValueError):  # email without '@' symbol
            Customer(valid_first_name, valid_last_name, 'test.bg', valid_phone_number, valid_address)
        with self.assertRaises(ValueError): # phone number should be 10 digits 
            Customer(valid_first_name, valid_last_name, valid_email, '123456789', valid_address) 
        with self.assertRaises(ValueError): # address should contain letters and be from 5 to 100 characters 
            Customer(valid_first_name, valid_last_name, valid_email, valid_phone_number, '123')
        
    


    def test_strMethod_whenCorrect(self):
        customer = Customer('Test', 'Test', 'Test@abv.bg', '1234567890', '123 Test Street, Test City, Test Country')

        valid_str = (
        'Customer: Test Test\n'
        'Email: Test@abv.bg\n'
        'Phone: 1234567890\n'
        'Address: 123 Test Street, Test City, Test Country')

        self.assertEqual(valid_str, str(customer))