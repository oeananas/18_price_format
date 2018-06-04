import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_pos_int_price(self):
        result = format_price('456700')
        self.assertEqual(result, '456 700')

    def test_neg_int_price(self):
        result = format_price('-6530000')
        self.assertEqual(result, 'the price must be a positive number!')

    def test_pos_float_price_without_fraction(self):
        result = format_price('3245.000000')
        self.assertEqual(result, '3 245')

    def test_pos_float_price_with_fraction(self):
        result = format_price('3245.68000')
        self.assertEqual(result, '3 245, 68')

    def test_neg_float_price(self):
        result = format_price('-7845.63000')
        self.assertEqual(result, 'the price must be a positive number!')

    def test_not_number_price(self):
        result = format_price('Hello!')
        self.assertEqual(result, 'this is not a price!')


if __name__ == '__main__':
    unittest.main()
