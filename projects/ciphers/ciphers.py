alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
import math
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
    simplePlain = simplify_string(plain)
    simpleKey = simplify_string(key)
    usingKeyChar = 0
    encoded = ''
    for c in simplePlain:
        if usingKeyChar >= len(simpleKey):
            usingKeyChar = 0
        keyChar = simpleKey[usingKeyChar]
        shiftedChar = shift_char(c, keyChar)
        encoded += shiftedChar
        usingKeyChar += 1
    return encoded

def vigenere_dec(cipher, key):
    simpleCipher = simplify_string(cipher)
    simpleKey = simplify_string(key)
    usingKeyChar = 0
    decoded = ''
    for c in simpleCipher:
        if usingKeyChar >= len(simpleKey):
            usingKeyChar = 0
        keyChar = simpleKey[usingKeyChar]
        keyIndex = let_to_num(keyChar)
        revKeyIndex = keyIndex * -1
        revKeyChar = num_to_let(revKeyIndex)
        shiftedChar = shift_char(c, revKeyChar)
        decoded += shiftedChar
        usingKeyChar += 1
    return decoded

#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    currentPart = 0
    splitStrings = []
    for c in s:
        # keep int currentParts less than parts minus one to stay inside array bounds
        if currentPart > parts - 1:
            currentPart = 0
        # if the array already has been initialized with as many indexes as part, append to string
        if len(splitStrings) >= parts:
            splitStrings[currentPart] += c
        # otherwise, add a new index with a single character as the string
        else:
            splitStrings.append(c)
        currentPart += 1
    return splitStrings
        
def vig_break_for_length(cipher, klen, frequencies):
   splitStrings = split_string(cipher, klen)
   key = ''
   for s in splitStrings:
       thisCaesarDec = caesar_break(s, english_freqs)
       # we can simply append to the key string w/out specifying order because python will run the loop one after another
       key += thisCaesarDec[0]
   return key

def vig_break(c, maxlen, frequencies):
    decAttempts = []
    # find best key for each possible key length
    for x in range(1, maxlen + 1):
        thisAttempt = vig_break_for_length(c, x, frequencies)
        decAttempts.append(thisAttempt)
    # decode ciphertext with each found key
    plainAttempts = []
    for key in decAttempts:
        thisPlain = vigenere_dec(c, key)
        plainAttempts.append({ 'key': key, 'plain': thisPlain })
    # find key that produces the least distance from 
    bestDistance = float('inf')
    bestKey = None
    for attempt in plainAttempts:
        # find and normalize letter counts
        decodeAttemptCounts = letter_counts(attempt['plain'])
        normDecodeAttempt = normalize(decodeAttemptCounts)
        # calculate distance from normal letter frequency
        attemptDistance = distance(normDecodeAttempt, frequencies)
        # if this is the smallest distance yet, set best vars equal to key and distance
        # if two keys have the same distance, the longer one will be compared second and will not be less than
        # the first key, so vig_break will return the shorter key
        if attemptDistance < bestDistance:
            bestDistance = attemptDistance
            bestKey = attempt['key']
    # decode the text according to best key and return
    decoded = vigenere_dec(c, bestKey)
    return [bestKey, decoded]

#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    # # generates an array of all 26 letters, arranged randomly
    key = list(alpha)
    random.shuffle(key)
    return key

def sub_enc(s, k):
    encoded = ''
    for c in s:
        # find position if char in alphabet
        charIndex = let_to_num(c)
        # find char position on scrambled alphabet
        encChar =  k[charIndex]
        # replace character with char from scrambled alphabet and append to encoded string
        encoded += encChar
    return encoded


def sub_dec(s, k):
    decoded = ''
    for c in s:
        # find position of char in key
        charIndex = k.index(c)
        # find letter that corresponds to index in actual alphabet
        decChar = alpha[charIndex]
        # append decoded character to decoded string
        decoded += decChar
    return decoded

#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    trigrams = {}
    for i, c in enumerate(s):
        trigram = s[i:i+3]
        if len(trigram) == 3:
            if trigram in trigrams:
                trigrams[trigram] += 1
            else:
                trigrams[trigram] = 1
    return trigrams

hitch = file_to_string('hitchhikers.txt')
simpleHitch = simplify_string(hitch)

# Uncomment the code below once the functions above are complete
english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

def map_log(d):
    lnd = {}
    for t in d:
        lnd[t] = math.log(d[t])
    return lnd

# Uncomment the code below once the functions above are complete
map_log(english_trigrams) 

def trigram_score(s, english_trigrams):
    score = 0
    sTri = count_trigrams(s)
    lnSTri = map_log(sTri)
    for t in lnSTri:
        if t not in english_trigrams:
            score -= 15
        else:
            score += math.log(english_trigrams[t])
    return score

def swapTwo(k):
    newK = k
    first = random.randint(0, 25)
    second = random.randint(0, 25)
    newK[first], newK[second] = newK[second], newK[first]
    return newK

def sub_break(cipher, english_trigrams):
    randKey = sub_gen_key()
    bestKey = randKey
    decAttempt = sub_dec(cipher, randKey)
    decScore = trigram_score(decAttempt, english_trigrams)
    bestScore = decScore
    nSinceImprovement = 0
    while nSinceImprovement <= 1000:
        tryKey = swapTwo(randKey[:])
        decAttempt = sub_dec(cipher, tryKey)
        decScore = trigram_score(decAttempt, english_trigrams)
        if decScore > bestScore:
            bestScore = decScore
            randKey = tryKey
            nSinceImprovement = 0
        else:
            nSinceImprovement += 1
    decrypted = sub_dec(cipher, randKey)
    return (bestKey, decrypted)

mystery = file_to_string('mystery3.txt')
print(sub_break(mystery, english_trigrams))

