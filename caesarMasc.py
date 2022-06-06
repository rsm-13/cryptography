import string as sm

def genCaesarAlpha(k):
    alpha = {}
    alphabet = sm.ascii_lowercase

    for i in range(len(alphabet)):
        alpha[alphabet[i]] = alphabet[(i + k) % 26].lower()

    return alpha

def find_caesar_shift(text):
    text = text.lower()
    chi = []

    for i in range(25):
        shifted = masc(text.lower(), genCaesarAlpha(i))
        chi.append(chi_squared_test(shifted))
        shift = chi.index(min(chi))

    print("The shift is: " + str((shift - 26)))

    return(masc(text.lower(), genCaesarAlpha(shift - 26)).lower())

def chi_squared_test(text):
    text = text.lower()
    alphabet = sm.ascii_lowercase

    freqEng = {'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40, \
    'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51, \
    'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28, \
    'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}

    chi_sq = 0

    for i in alphabet:
        e_sub_i = (freqEng[i] * (len(text))) / 100
        chi_sq += ((((text.count(i)) - (e_sub_i)) ** 2) / (e_sub_i))

    return chi_sq

def revDict(letters):
    dictRev = {}
    for key in letters:
        dictRev[letters[key].upper()] = key.lower()
    return dictRev

def masc(text, alpha):
    #Create the string for text
    ct = ''
    #Loop through the characters in text
    for char in text:
        #Maintain whitespace
        if char in sm.whitespace:
            ct += char
        #Remove any punctuation
        elif char in sm.punctuation:
            continue
        #Convert everything else using dictionary
        else:
            ct += alpha[char]

    return ct

def brute_force(text):
    possible = []

    for i in range(25):
        temp = masc(text, revDict(genCaesarAlpha(i)))
        possible.append(temp)

    return possible

def main():
    choice = int(input("What would you like to do?\n[1] Encrypt with Caesar\n[2] Decrypt with Caesar\n[3] Break Caesar using brute force\n[4] Decrypt with Chi-Sq. Test\n"))
    text = ''
    k = int(input("Input the shift if applicable. Negative for decryption. If not, use '0'"))

    if choice == 1:
        text = str(input("Input the plaintext here."))
        alpha = genCaesarAlpha(k)
        finalText = masc(text.lower(), alpha).upper()

    elif choice == 2:
        text = str(input("Input the ciphertext here."))
        alpha = genCaesarAlpha(k)
        finalText = masc(text.lower(), alpha).lower()

    elif choice == 3:
        with open("instructions.txt") as f:
            text = f.read()
        finalText = ''

        alpha = genCaesarAlpha(k)
        finalText = masc(text.upper(), revDict(genCaesarAlpha(k)))

        for option in brute_force(text):
            finalText += option + '\n\n'

    elif choice == 4: # Find Caesar Shift + Decrypt with Chi-Squared Test
        text = str(input("Input the ciphertext here.")).upper()
        finalText = find_caesar_shift(text)

    print_or_file = int(input("Would you like to print the result or write it into a new file? Type '1' to print and '2' to file."))

    if print_or_file == 1:
        return finalText

    elif print_or_file == 2:
        file_name = str(input("What would you like to call the file? Please add the file type at the end."))
        with open(file_name, 'w') as w:
            w.write(finalText)
        return "This has been written into the file, " + file_name + "."

    else:
        pass

print(main())
