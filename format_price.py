import sys


def format_price(price):
    if type(price) is str:
        try:
            float_price = float('{0:.2f}'.format(float(price)))
        except ValueError:
            return None
        price_parts = str(float_price).split('.')
        whole_part, fract_part = price_parts[0], price_parts[1]
        if not float_price.is_integer():
            pretty_price = '{:,}.{}'.format(
                int(whole_part),
                fract_part
            ).replace(',', ' ')
        else:
            pretty_price = '{:,}'.format(int(whole_part)).replace(',', ' ')
        return pretty_price


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you need to enter parameter')
    price = sys.argv[1]
    print(format_price(price))
