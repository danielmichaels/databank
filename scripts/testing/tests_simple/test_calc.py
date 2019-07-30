import unittest
import calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        # return super().setUp()
        pass

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)

    def test_multiply(self):
        result = calc.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
