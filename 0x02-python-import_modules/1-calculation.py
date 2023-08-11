#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)
print(f"{a:d} + {b:d} = {add_result:d}".format(a, b, add_result))
print(f"{a:d} - {b:d} = {sub_result:d}".format(a, b, sub_result))
print(f"{a:d} * {b:d} = {mul_result:d}".format(a, b, mul_result))
print(f"{a:d} / {b:d} = {div_result:d}".format(a, b, div_result))
