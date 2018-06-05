# Price Formatter

script for formatting prices.
As an argument, a line with a price is indicated, after which the program converts the data into a more intuitive form.

# QuickStart

Example of script launch on Linux, Python 3.5

launch on console:

```bash
python3 format_price.py 123323.000000 
123 323

python3 format_price.py 35889787
35 889 787

python3 format_price.py -546788
-546 788
```
launch on program:
```python3
from format_price import format_price


price1 = 123888
print(format_price(price1))
price2 = 'hello2233'
print(format_price(price2))
price3 = '99345.0000000'
print(format_price(price3))
price4 = '6788999'
print(format_price(price4))
```
output:
```bash
None
None
99 345
6 788 999
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
