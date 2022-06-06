import string as sm

def genCaesarAlpha(k):  # Encrypt / Decrypt Using Caesar
    alpha = {}
    alphabet = sm.ascii_lowercase

    # Create a dictionary with the shift based on k
    for i in range(len(alphabet)):
        alpha[alphabet[i]] = alphabet[(i + k) % 26].lower()

    return alpha

def masc(text, alpha):  # MonoAlphabetic Substitution Method
    # Create the string for text
    ct = ''
    # Loop through the characters in text
    for char in text:
        # Maintain whitespace
        if char in sm.whitespace:
            ct += char
        # Remove any punctuation
        elif char in sm.punctuation:
            continue
        # Convert everything else using dictionary
        else:
            ct += alpha[char]

    return ct

def remove_chars(word1, word2):
    for char in word1:
        word2 = word2.replace(char, "")
    return word2

def remove_duplicates(word):
    new = ""
    for char in word: 
        if char not in new:
           new += char
    return new

def vigenere(text, choice, kw):   # Vignère Cipher (Encryption & Decryption)
    alphabet = sm.ascii_lowercase
    key = []
    kw_index = 0

    for i in range(len(text)):
        # Maintain Spaces
        if text[i] == " ":
            key.append(" ")
        
        # Create a list of the repeating keyword for the length of the text
        else:
            i = kw_index % len(kw)
            key.append(kw[i])
            kw_index += 1

    final_text = ""

    for i in range(len(text)):
        # Keep Spaces in ct
        if text[i] == " ":
            final_text += " "

        # Encrypt / Decrypt with Vigènere and Tabula Recta Alphabets
        else:
            if choice == 1: # Encrypt with Vigènere
                final_text += alphabet[(alphabet.find(text[i]) + alphabet.find(key[i])) % 26]
                final_text = final_text.upper()

            elif choice == 2:   # Decrypt with Vigènere
                final_text += alphabet[(alphabet.find(text[i]) - alphabet.find(key[i])) % 26]
                final_text = final_text.lower()

    return final_text

def split_chars(text, value):
    text = ''.join([str(char) for char in text if char not in sm.whitespace])
    output = [text[i::value] for i in range(value)]
    return output

def find_closest(nums, value):
    difference = [abs(value - n) for n in nums]
    return difference.index(min(difference))

def find_IC(text):
    total = 0 
    text = (''.join([str(c) for c in text if c not in sm.whitespace])).lower()
    
    for i in remove_duplicates(text):
        total += text.count(i) * (text.count(i) - 1)
    total = total / (len(text) * (len(text) - 1))

    return total
        
def vigenere_keylength(n, text):
    engIC = 0.06612
    avgICs = []

    for i in range(1, n):
        #kw 1, finds the IC for each line in the charsplitted text
        avgICs.append(sum([find_IC(j) for j in split_chars(text, i)]) / i)
    #kw length n is index +1

    return ((find_closest(avgICs, engIC)) + 1)

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

def find_keyword(text):
    alphabet = sm.ascii_lowercase
    n = int(input("Input n for kl."))
    kl = vigenere_keylength(n, text)
    #kl = int(input("Input kl"))
    text_splits = split_chars(text, kl)

    chi = []
    shifts = []
    keyword = ''

    for i in range(kl):
        chi.append([])
        for j in range(25):
            shifted = masc(text_splits[i].lower(), genCaesarAlpha(j))
            chi[i].append(chi_squared_test(shifted))
        shifts.append(chi[i].index(min(chi[i])))
        keyword += alphabet[-1 * shifts[i]]
        
    print("The keyword is: " + keyword)
    return keyword

def decrypt_vigenere(text):
    final = vigenere(text, 2, find_keyword(text))

    return final

def main():
	
    # Asking About Encryption vs. Decryption
    choice = int(input("What would you like to do?\n[1] Encrypt with Vigenère\n[2] Decrypt with Vigènere (with keyword)\n[3] Decrypt with Vigenère w/o Keyword\n[4] Find Chi-Squared Value\n[5] Find Index Coincidence\n"))
    text = str(input("Input the text here."))

    if choice == 1 or choice == 2: # Encrypt / Decrypt with Vigènere
        kw = str(input("Input the keyword.")).upper()
        finaltext = vigenere(text, choice, kw)
    
    elif choice == 3:
        text = text.replace(" ", "")
        text = text.lower()
        finaltext = decrypt_vigenere(text)
        
    elif choice == 4:
        text = text.replace(" ", "")
        finaltext = chi_squared_test(text)

    elif choice == 5:
        text = text.replace(" ", "")
        finaltext = find_IC(text)

    # Ask about how to give output text
    print_or_file = int(input("Would you like to print the result or write it into a new file? Type '1' to print and '2' to file."))

    if print_or_file == 1:
        print(finaltext)

    elif print_or_file == 2:
        file_name = str(input("What would you like to call the file? Please add the file type at the end."))
        with open(file_name, 'w') as w:
            w.write(finaltext)
        return "This has been written into the file, " + file_name + "."

    else:
        pass

main()   # Run Main Function to do All Operations