temp = int(input("what is the temperature outside: ".capitalize()))

if temp>= 0 and temp<= 25:
    print("The temperature is cool")
elif temp>25 and temp<=35:
    print("The temperature is good")
elif temp>35 and temp<50:
    print("The temperature is hot")
elif temp<0 or temp >50: 
    print("The temperture is terible outslide")
