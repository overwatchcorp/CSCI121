alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
random.seed()

#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string, 
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s):
    sAlpha = [ c for c in s.upper() if c in alpha ]
    simpleString = ''.join(sAlpha)
    return simpleString

def num_to_let(x):
    letterSpace = len(alpha)
    if x >= letterSpace:
        x -= letterSpace
    i = alpha[x]
    return i

def let_to_num(a):
    c = a.upper()
    xIndex = alpha.index(c)
    return xIndex

def shift_char(char, shift):
    # get positions of letters in alphabet
    charIndex = let_to_num(char)
    shiftBy = let_to_num(shift)
    # shift char to new position
    newCharIndex = charIndex + shiftBy
    # if new character is at the end, move char index back to beginning
    letterSpace = len(alpha)
    if newCharIndex > letterSpace:
        newCharIndex -= letterSpace
    newChar = num_to_let(newCharIndex)
    return newChar

def caesar_enc(plain, key):
    simplePlain = simplify_string(plain)
    encodedChars = [ shift_char(c, key) for c in simplePlain ]
    caesarEncoded = ''.join(encodedChars)
    return caesarEncoded

def caesar_dec(cipher, key):
    keyIndex = let_to_num(key)
    reversedKey = -1 * keyIndex
    decKey = num_to_let(reversedKey)
    encodedChars = [ shift_char(c, decKey) for c in cipher ]
    caesarEncoded = ''.join(encodedChars)
    return caesarEncoded

#############################################################
# Breaking the Caesar cipher
#############################################################

def add_to_dict(c, d):
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
    return d

def letter_counts(s):
    counts = {}
    [ add_to_dict(c, counts) for c in s ]
    return counts

def normalize(counts):
    totalChars = 0
    for count in counts:
        totalChars += counts[count]
    for count in counts:
        counts[count] = counts[count] / totalChars
    return counts

# Uncomment the code below once the functions above are complete
english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_freqs)


def distance(observed, expected):
    totalDistance = 0
    for c in observed:
        thisDistance = ((observed[c] - expected[c]) ** 2) / expected[c]
        totalDistance += thisDistance
    return totalDistance

def caesar_break(cipher, frequencies):
    lowestDistance = float('inf')
    lowestKey = None
    for c in frequencies:
        decodeAttempt = caesar_dec(cipher, c)
        decodeAttemptCounts = letter_counts(decodeAttempt)
        normDecodeAttempt = normalize(decodeAttemptCounts)
        attemptDistance = distance(normDecodeAttempt, frequencies)
        if attemptDistance < lowestDistance:
            lowestDistance = attemptDistance
            lowestKey = c
    decoded = caesar_dec(cipher, lowestKey)
    return [lowestKey, decoded]

#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    "your code here"

def vigenere_dec(cipher, key):
    "your code here"


#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    "your code here"

def vig_break_for_length(cipher, klen, frequencies):
    "your code here"

def vig_break(c, maxlen, frequencies):
    "your code here"



#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    "your code here"

def sub_enc(s, k):
    "your code here"

def sub_dec(s, k):
    "your code here"


#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    "your code here"

# Uncomment the code below once the functions above are complete
# english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
# normalize(english_trigrams)

def map_log(d):
    "your code here"

# Uncomment the code below once the functions above are complete
# map_log(english_trigrams) 

def trigram_score(s, english_trigrams):
    "your code here"

def sub_break(cipher, english_trigrams):
    "your code here"



