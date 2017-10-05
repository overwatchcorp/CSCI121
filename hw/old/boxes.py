width = int(input("Width? "))
number = int(input("Number? "))

topOrBottomOfBox = "+" + "-" * width + "+"
topOrBottom = (topOrBottomOfBox + " ") * number
topOrBottomWithoutExtraSpace = topOrBottom[:-1]

middleOfBox = ("|" + " " * (width) + "|")
middle = (middleOfBox + " ") * number
middleWithoutExtraSpace = middle[:-1]

print()
print(topOrBottomWithoutExtraSpace)
print(middleWithoutExtraSpace)
print(topOrBottomWithoutExtraSpace)
