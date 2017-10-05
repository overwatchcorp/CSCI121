word = input("Word? ")
wordLength = len(word)

marqueeBorderLength = 4 + wordLength
marqueeBorder = "*" * marqueeBorderLength

print()
print(marqueeBorder)
print("* " + word + " *")
print(marqueeBorder)
