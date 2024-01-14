import unittest
import dummy

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(dummy.add(10, 5), 15)
        self.assertEqual(dummy.add(-1, 1), 0)
        self.assertEqual(dummy.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(dummy.sub(10, 5), 5)
        self.assertFalse(dummy.sub(10, 6) == 5)
        self.assertEqual(dummy.sub(-1, 1), -2)
        self.assertEqual(dummy.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(dummy.mul(10, 5), 50)
        self.assertEqual(dummy.mul(-1, 1), -1)
        self.assertEqual(dummy.mul(-1, -1), 1)

    def test_div(self):
        self.assertEqual(dummy.div(10, 5), 2)
        self.assertFalse(dummy.div(2, 2) == 2.5)
        self.assertEqual(dummy.div(-1, 1), -1)
        self.assertEqual(dummy.div(-1, -1), 1)
       

        with self.assertRaises(ValueError):
            dummy.div(10, 0)



if __name__ == "__main__":
    unittest.main()
