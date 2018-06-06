import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_pos_int_price(self):
        pretty_price = format_price('456700')
        self.assertEqual(pretty_price, '456 700')

    def test_neg_int_price(self):
        pretty_price = format_price('-6530000')
        self.assertEqual(pretty_price, '-6 530 000')

    def test_pos_float_price_without_fraction(self):
        pretty_price = format_price('3245.000000')
        self.assertEqual(pretty_price, '3 245')

    def test_pos_float_price_with_fraction(self):
        pretty_price = format_price('3245.68000')
        self.assertEqual(pretty_price, '3 245.68')

    def test_neg_float_price(self):
        pretty_price = format_price('-7845.63000')
        self.assertEqual(pretty_price, '-7 845.63')

    def test_pos_int_number(self):
        pretty_price = format_price(456700)
        self.assertEqual(pretty_price, '456 700')

    def test_neg_int_number(self):
        pretty_price = format_price(-6530000)
        self.assertEqual(pretty_price, '-6 530 000')

    def test_pos_float_number_without_fraction(self):
        pretty_price = format_price(3245.000000)
        self.assertEqual(pretty_price, '3 245')

    def test_pos_float_number_with_fraction(self):
        pretty_price = format_price(3245.68000)
        self.assertEqual(pretty_price, '3 245.68')

    def test_neg_float_number(self):
        pretty_price = format_price(-7845.63000)
        self.assertEqual(pretty_price, '-7 845.63')

    def test_str_not_number_price(self):
        pretty_price = format_price('Hello!')
        self.assertIsNone(pretty_price)

    def test_lst_not_number_price(self):
        pretty_price = format_price([1, 2, 3])
        self.assertIsNone(pretty_price)

    def test_dict_not_number_price(self):
        pretty_price = format_price({'Russia': 'Moscow'})
        self.assertIsNone(pretty_price)

    def test_tup_not_number_price(self):
        pretty_price = format_price(('Hello!', 'Hi'))
        self.assertIsNone(pretty_price)

    def test_none_price(self):
        pretty_price = format_price(None)
        self.assertIsNone(pretty_price)

    def test_bool_price(self):
        pretty_price = format_price(True)
        self.assertIsNone(pretty_price)


if __name__ == '__main__':
    unittest.main()
