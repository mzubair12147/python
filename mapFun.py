# map method apply a function to each item in an iterable(list, tuple, etc)

store = [("shirt", 40), ("pants", 45), ("jackets", 100), ("socks", 20), ("suit", 200)]

priceINRToPKR = lambda item: (item[0], item[1] * 3.25)

storePKR = map(priceINRToPKR, store)

for item in storePKR:
    print(f"{item[0]}: {item[1]}")
