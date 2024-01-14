import unittest
from employee import Employee as emp

class test_employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup class')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp1 = emp('Antony', 'Baragu', 1000)
        self.emp2 = emp('John', 'Ngechu', 1200)


    def tearDown(self):
        print('teardown')

    def test_email(self):
        print('email test')
        self.assertEqual(self.emp1.email, 'Antony.Baragu@email.com')
        self.assertEqual(self.emp2.email, 'John.Ngechu@email.com')
    def test_fullname(self):
        print("test full name")
        self.assertEqual(self.emp1.fullname, 'Antony Baragu')
        self.assertEqual(self.emp2.fullname, 'John Ngechu')

    def test_apply_raise(self): 
        print("apply raise")
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.pay, 1050)

if __name__ == "__main__":
    unittest.main()
