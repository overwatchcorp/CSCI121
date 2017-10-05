name = input("Restaurant name? ")
entree1 = input("First entree? ")
entree1Price = int(input("First entree price? "))
entree2 = input("Second entree? ")
entree2Price = int(input("Second entree price? "))
entree3 = input("Third entree? ")
entree3Price = int(input("Third entree price? "))

print("\n1234567890123456789012345678901234567890\n")

title = name + " Entrees"
print(title)
print("-" * len(title))
entree1Length = len(entree1)
entree1PriceLength = len(str(entree1Price))
entree2Length = len(entree2)
entree2PriceLength = len(str(entree2Price))
entree3Length = len(entree3)
entree3PriceLength = len(str(entree3Price))
menuEntryLength = 36
print(entree1 + ("." * (menuEntryLength - entree1Length)) + "$" + (" " * (3 - entree1PriceLength)) + str(entree1Price))
print(entree2 + ("." * (menuEntryLength- entree2Length)) + "$" + (" " * (3 - entree2PriceLength)) + str(entree2Price))
print(entree3 + ("." * (menuEntryLength - entree3Length)) + "$" + (" " * (3 - entree3PriceLength)) + str(entree3Price))
