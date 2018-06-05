import sys


def format_price(price):
    try:
        float_price = float(str(price))
    except(ValueError, TypeError):
        return None
    pretty_price = '{:,.0f}'.format(float_price).replace(',', ' ')
    return pretty_price


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you need to enter parameter')
    price = sys.argv[1]
    print(format_price(price))
