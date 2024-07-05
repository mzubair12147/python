# filter function: creates a collection of elements of an iterable for which a function returns true
store = [("shirt", 40), ("pants", 45), ("jackets", 100), ("socks", 20), ("suit", 200)]

filterProducts = lambda product: product[1] < 100

# it returns a filter object, so we need to convert it into a list.
productHighPrice = filter(filterProducts, store)
print(productHighPrice)
for i in productHighPrice:
    print(i)
