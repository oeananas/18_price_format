import sys


def format_price(price):
    try:
        float_price = float('{}'.format(float(price)))
    except(ValueError, TypeError):
        return None
    if not float_price.is_integer():
        pretty_price = '{:,.2f}'.format(float(float_price), ).replace(',', ' ')
    else:
        pretty_price = '{:,}'.format(int(float_price), ).replace(',', ' ')
    return pretty_price


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you need to enter parameter')
    price = sys.argv[1]
    print(format_price(price))
