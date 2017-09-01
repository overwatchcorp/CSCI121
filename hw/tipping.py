priceDollars = int(input("Price dollars? "))
priceCents = int(input("Price cents? "))
totalPrice = priceDollars + (priceCents / 100)

tipPercent = int(input("Tip percentage [0-100]? ")) / 100 

# print((math.floor(totalPrice * tipPercent * 100) / 10))
print(totalPrice * tipPercent)
