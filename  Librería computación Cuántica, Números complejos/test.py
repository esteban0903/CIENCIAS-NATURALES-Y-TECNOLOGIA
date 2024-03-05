import unittest
import Operations as lc


class TestStringMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(lc.addition((1, 2), (3, 4)), (4, 6))
        self.assertEqual(lc.addition((-1, -2), (3, 4)), (2, 2))

    def test_multiplication(self):
        self.assertEqual(lc.multiplication((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(lc.multiplication((-1, -2), (3, 4)), (5, -10))

    def test_subtraction(self):
        self.assertEqual(lc.subtraction((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(lc.subtraction((-1, -2), (3, 4)), (-4, -6))

    def test_division(self):
        self.assertEqual(lc.division((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(lc.division((-1, -2), (3, 4)), (-0.44, -0.08))

    def test_modulus(self):
        self.assertEqual(lc.modulus((2, 2)), 2.83)
        self.assertEqual(lc.modulus((10, 10)), 14.14)

    def test_conjugate(self):
        self.assertEqual(lc.conjugate((1, 5)), (1, -5))
        self.assertEqual(lc.conjugate((4, -9)), (4, 9))

    def test_phase(self):
        self.assertEqual(lc.phase((5, 5)), 0.79)
        self.assertEqual(lc.phase((0, 8)), 1.57)

    def test_cartesian_polar(self):
        self.assertEqual(lc.cartesian_polar((1, 2)), (2.24, 1.11))
        self.assertEqual(lc.cartesian_polar((3, 4)), (5, 0.93))

    def test_polar_cartesian(self):
        self.assertEqual(lc.polar_cartesian((2.24, 1.11)), (1, 2.01))
        self.assertEqual(lc.polar_cartesian((5, 0.93)), (2.99, 4.01))

if __name__ == '__main__':
    unittest.main()
