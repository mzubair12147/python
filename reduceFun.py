# reduce() : apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeat this process until 1 value remains.
# reduce(function, iterable)

import functools

store = [("shirt", 40), ("pants", 45), ("jackets", 100), ("socks", 20), ("suit", 200)]

priceSum = functools.reduce(lambda a, b,: a + b, map(lambda item: item[1], store))

print(priceSum)
