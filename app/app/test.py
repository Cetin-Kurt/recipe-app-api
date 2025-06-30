"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 21)

    def test_add_numbers_negative(self):
        """Test adding negative numbers"""
        res = calc.add(-5, -6)
        self.assertEqual(res, -11)

    def test_add_numbers_zero(self):
        """Test adding zero"""
        res = calc.add(0, 0)
        self.assertEqual(res, 0)