# importing in python is the process of loading code from a python module into the current script.
# this allows us to use the functions and variables defined in the module in your current script.
# and also any individual modules that the imported module may depend on.


# WAY 1:
# import math
# result = math.sqrt(121)
# print(result)


# WAY 2:
# from math import sqrt, pi
# result = sqrt(9)*pi
# print(result)


# # WAY 3:
# import math as m
# result = m.sqrt(9) * m.pi
# print(result)


# # WAY 4:
# import math as math_builtin_python
# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)


# import math
# print(dir(math)) # now this will print all the in-built functions inside "math" library
# print(math.nan, type(math.nan))

from antash import welcome, antash
welcome()
print(antash)