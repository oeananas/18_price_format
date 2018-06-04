import sys


def format_price(price):
    try:
        float_price = float(price)
    except ValueError:
        return 'this is not a price!'
    if float_price > 0:
        price_parts = str(float_price).split('.')
        whole_part = price_parts[0]
        fract_part = price_parts[1]
        pretty_whole_part = '{0:,}'.format(int(whole_part)).replace(',', ' ')
        if int(fract_part) != 0:
            pretty_fract_part = fract_part[:2]
            pretty_price = '{}, {}'.format(pretty_whole_part,
                                           pretty_fract_part)
            return pretty_price
        else:
            return pretty_whole_part
    else:
        return 'the price must be a positive number!'


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you need to enter parameter')
    price = sys.argv[1]
    print(format_price(price))
