from employee import Employee
import unittest

class testEmployee(unittest.TestCase):
    def setUp(self):
        self.raises = ['',1000]
        self.my_employee = Employee('cucu', 'lopez', 1000)

    def test_default_raise(self):
        self.my_employee.give_raise(self.raises[0])
    
    def test_custom_raise(self):
        self.my_employee.give_raise(self.raises[1])

if __name__ == '__main__':
    unittest.main()