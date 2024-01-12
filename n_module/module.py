import calc_add
# import calc.calc_sub
# import calc.calc_sub as sub
from calc.calc_sub import sub
from calc.calc import Calculator


import os
import sys

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == '__main__':
#     print(calc_add.add(1, 3))
#     # print(sub.sub(4, 5))
#     print(sub(4, 5))
#     print("=" * 20)
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())



