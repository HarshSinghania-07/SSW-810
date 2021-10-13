'''

NAME: HARSH SINGHANIA
HW03- FRACTION TEST
CWID- 20007289
Test case file for the Fraction class python file with the additional operations mentioned in the problem statement. Using unittest we can see if each 
operation of the code is fit for use.

'''

import unittest
from HW03_Harsh_Singhania import Fraction 

class TestFraction(unittest.TestCase):
    def test_init(self):
        """To verify that the numerator and denominator are set properly. """
        ftest: Fraction = Fraction(3, 4)
        self.assertEqual(ftest.numerator, 3)
        self.assertEqual(ftest.denominator, 4)
        with self.assertRaises(ValueError):
            Fraction(1,0)

    def test_init_exception(self) :
        """ To verify that ValueError is raised when appropriate. """
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_add(self) :
        """ To verify Fraction addition operation. """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  

    def test_sub(self):
        """ To verify Fraction subtraction operation. """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-1, 4))
        self.assertEqual(f12, Fraction(1, 2))

    def test_mul(self):
        """ To verify Fraction multiplication operation. """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12, Fraction(1, 2))

    def test_truediv(self):
        """ To verify Fraction division operation. """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 / f34, Fraction(2, 3))
        self.assertEqual(f12, Fraction(1, 2))

    def test_str(self):
        """To verify string"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(str(f12), ('1 / 2'))

    def test_ne(self):
        """To verify not equal function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertNotEqual(f12, f34)
        self.assertNotEqual(f34, f12)
        self.assertNotEqual(f23, f12)
        self.assertFalse(f12 != f12)

    def test_eq(self):
        """To verify equal function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 == f12)
        self.assertFalse(f12 == f34)
        self.assertTrue(f34 == f34)
        self.assertEqual(f12, f12)
        self.assertFalse(f23 == f12)

    def test_le(self):
        """To verify Less than or equal function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 <= f12)
        self.assertTrue(f12 <= f34)
        self.assertTrue(f34 <= f34)
        self.assertLessEqual(f12, f12)
        self.assertLessEqual(f23, f12)

    def test_lt(self):
        """To verify Less Than function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f12 < f34)
        self.assertFalse(f34 < f12)
        self.assertLess(f12, f34)
        self.assertLess(f23, f12)

    def test_ge(self):
        """To verify Greater Than or Equal function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f34 >= f12)
        self.assertFalse(f12 >= f34)
        self.assertTrue(f34 >= f34)
        self.assertGreaterEqual(f34, f12)
        self.assertGreaterEqual(f12, f23)

    def test_gt(self):
        """To verify Greater Than function of 2 fractions"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f23: Fraction = Fraction(-2, 3)
        self.assertTrue(f34 > f12)
        self.assertFalse(f12 > f34)
        self.assertGreater(f34, f12)
        self.assertGreater(f12, f23)


    def test_3_operands(self):
        """ To verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))
        self.assertTrue(f12 - f34 - f44 == Fraction(-40, 32))
        self.assertTrue((f12 * f34 * f44 == Fraction(12, 32)))
        self.assertTrue((f12 / f34 / f44 == Fraction(16, 24)))

if __name__ == '__main__':
    """verbosity = 0(quite) : Just get total nof tests executed and global result
        verbosity = 1(default) : You get same as ) but dot for every successful test or F for failure
        verbosity = 2(Verbose) : You get help string of every test and the result
    """
    unittest.main(exit=False, verbosity=2)