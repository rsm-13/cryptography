import matplotlib.pyplot as plt # Mat Plot Lib to Create Histogram to be called as 'plt'
import string as sm     # String Module to be called as 'sm'

def genCaesarAlpha(k):  # Encrypt / Decrypt Using Caesar
    alpha = {}
    alphabet = sm.ascii_lowercase

    # Create a dictionary with the shift based on k
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

def gen_kwd_dict(keyword):  # Encrypt using Keyword
    alpha = {}
    alphabet = sm.ascii_lowercase

    # Remove whitespaces and punct. from keyword
    for char in keyword:
        if char in sm.whitespace:
            keyword = keyword.replace(char, "")
        elif char in sm.punctuation:
            keyword = keyword.replace(char, "")

    # Assign lowercase alphabet as keys
    keys = [char for char in alphabet]
    keys = list("".join(dict.fromkeys(alphabet)).lower())
    # Remove any duplicate letters and assign as values
    values = list("".join(dict.fromkeys(keyword)).upper())

    # Find index of last char of keyword to create the
    # Remainder of values from beg/end of alphabet
    lastIndex = values[-1].lower()
    index = alphabet.index(lastIndex) + 1
    end_alphabet = alphabet[index:]
    beg_alphabet = alphabet[:index]

    # Add values to end of dictionary
    for char in end_alphabet:
        values.append(char.upper())

    for char in beg_alphabet:
        values.append(char.upper())

    values = "".join(dict.fromkeys(values)).upper()
    alpha = dict(zip(keys, values))

    return alpha

def letterFreqAlpha(count_vs_percent, text):    # Returning Frequency in % / # of Occurences
    alphabet = [char for char in sm.ascii_lowercase]
    text = text.lower()
    frequency_num = {}
    frequency_percent = {}

    for char in text:   # Scrubbing the text to be only letters
        if char in sm.whitespace:
            text = text.replace(char,'')
        elif char in sm.punctuation:
            text = text.replace(char,'')

    # Finding num of letters
    totalLength = len(text)

    for i in range(26):
        # Going through letters in the alphabet and assigning indices
        index = alphabet[i]
        # Find the number of occurences of each letter
        occurrence = text.count(index)
        # Assigning values into dictionary with keys being the letters
        frequency_num[index] = occurrence
        # Translating the number of occurences to percentages
        frequency_percent[index] = (occurrence / totalLength) * 100

    if count_vs_percent == 1:   # Return the number of occurences per each letter in a dictionary
        return frequency_num

    elif count_vs_percent == 2: # Print the number of occurences in a histogram with '<' notating the occurences
        for key in frequency_num.keys():
            print(key + '\t' + str(round(frequency_num[key], 1)) + '     ' + (">" * int(frequency_num[key])))

    elif count_vs_percent == 3: # Print the percentage of occurences for each letters
        for key in frequency_percent.keys():
            print(key + '\t' + str(round(frequency_percent[key], 1)) + '%')

    else:   # Frequency Analysis in percentages in a dictionary
        return frequency_percent

def printLetterFreqDecrease(frequency_percent): # Printing the Frequency of Chars in % in Descending Order
    # Sort the values in descending order
    sorted_values_descending = sorted(frequency_percent.values(), reverse = True)
    sorted_dict = {}

    for i in sorted_values_descending:
        for key in frequency_percent.keys():
            if frequency_percent[key] == i:
                sorted_dict[key] = frequency_percent[key]

    print("The frequencies in percentages are:")
    for key in sorted_dict.keys():
        # Frequency Analysis (Descending Order by %)
        print(key + '\t' + str(round(sorted_dict[key], 1)) + '%')

    return ""

def histogram(frequency_percent):   # Create a Bar Chart Showing Frequency Analysis
    # x-Coordinates of Left Sides of Bars
    keys = list(frequency_percent.keys())
    
    # Heights of Bars
    height = list(frequency_percent.values())
    
    # Labels for Bars
    alphabet = [char for char in sm.ascii_lowercase]
    tick_label = alphabet
    
    # Naming the x-axis
    plt.xlabel('Letters')
    # Naming the y-axis
    plt.ylabel('Frequencies in Percentage')
    # plot title
    plt.title('Frequency Histogram')

    # Plotting the Bar CHart
    plt.bar(keys, height, tick_label = tick_label,
        width = 0.8, color = ['powderblue'])
    
    # Function to Show the Chart
    return plt.show()

def printDigraph(text): # Return the Top 10 Digraphs from the Text
    alphabet = sm.ascii_uppercase
    text = text.upper()
    text = [char for char in text]
    digraphs = {}

    for i in range(len(text)-1):
        # Check every pair of two letters
        if text[i] in alphabet and text[i+1] in alphabet:
            # Create pair of letters
            pair = str(text[i] + text[i+1])
            # If the pair is not already in the dict, add & set equal to 1 instance
            if pair not in digraphs.keys():
                digraphs[pair] = 1
            # If the pair exists, increment the number of occurences by 1
            elif pair in digraphs.keys():
                digraphs[pair] += 1
    
    # Sort the values (instances) in decreasing order
    sorted_values_descending = sorted(digraphs.values(), reverse = True)
    sorted_dict = {}

    for i in sorted_values_descending:
        for key in digraphs.keys():
            if digraphs[key] == i:
                sorted_dict[key] = digraphs[key]

    # Show the top 10 occurences of digraphs
    top10digraphs = list(sorted_dict.keys())[:10]

    print("The top 10 digraphs are: " + ", ".join(top10digraphs) + '\n')
    return ""

def printTrigraph(text): # Return the Top 10 Trigraphs from the Text
    alphabet = sm.ascii_uppercase
    text = text.upper()
    text = [char for char in text]
    trigraphs = {}
    
    # Check every pair of three letters
    for i in range(len(text)-2):
        if str(text[i]) in alphabet and str(text[i+1]) in alphabet and str(text[i+2]) in alphabet:
            # Create pair of letters
            trio = str(text[i] + text[i+1] + text[i+2])
            # If the trio is not already in the dict, add & set equal to 1 instance
            if trio not in trigraphs.keys():
                trigraphs[trio] = 1
            # If the trio exists, increment the number of occurences by 1
            elif trio in trigraphs.keys():
                trigraphs[trio] += 1
    
    # Sort the values (instances) in decreasing order
    sorted_values_descending = sorted(trigraphs.values(), reverse = True)
    sorted_dict = {}

    for i in sorted_values_descending:
        for key in trigraphs.keys():
            if trigraphs[key] == i:
                sorted_dict[key] = trigraphs[key]

    # Show the top 10 occurences of trigraphs
    top10trigraphs = list(sorted_dict.keys())[:10]

    print("The top 10 trigraphs are: " + ", ".join(top10trigraphs) + '\n')
    return ""

def doubleLetters(text): # Return the Top 10 Digraphs from the Text
    alphabet = sm.ascii_uppercase
    text = text.upper()
    text = [char for char in text]
    digraphs = {}

    for i in range(len(text)-1):
        # Check every pair of two letters
        if text[i] in alphabet and text[i+1] in alphabet:
            # Create pair of letters
            pair = str(text[i] + text[i+1])
            # If the pair is not already in the dict, add & set equal to 1 instance
            if pair not in digraphs.keys():
                digraphs[pair] = 1
            # If the pair exists, increment the number of occurences by 1
            elif pair in digraphs.keys():
                digraphs[pair] += 1

    alphabet = [char for char in alphabet]
    doubleLetters = {}
    
    # Check every pair of letters
    for i in range(25):
        # Create a pair of double letters using alphabet letters
        double = str(alphabet[i]) + str(alphabet[i])
        # Check if the double-letter pair is in the digraphs dictionary
        if double in digraphs.keys():
            # If it exists, then add all instances of the double-letters to a dictionary
            doubleLetters[double] = digraphs[double]

    # Sort the values (instances) in decreasing order
    sorted_values_descending = sorted(doubleLetters.values(), reverse = True)
    sorted_doubles = {}

    for i in sorted_values_descending:
        for key in doubleLetters.keys():
            if doubleLetters[key] == i:
                sorted_doubles[key] = doubleLetters[key]

    # Show 5 most frequently occuring pair of double letters
    top5doubles = list(sorted_doubles.keys())[:5]
    
    print("The top 5 double letters are: " + ", ".join(top5doubles) + '\n')
    return ""
    
def swapLetters(ct_letter, pt_letter, text):    # Testing Replacing Different ct letters with pt letters (Using Frequency Analysis)
    newText = text.replace(ct_letter, pt_letter)
    
    return newText

def resetLetters(pt_letter, text, ct_letter):    # Reverting the Replacement --> pt (test) letters with ct (original) letters
    newText = text.replace(pt_letter, ct_letter)

    return newText

def frequencyAnalysis(text, digraph, trigraph, doubles, frequency):

    print(str(digraph) + str(trigraph) + str(doubles) + str(frequency))
    print("Here is the original ciphertext: \n\n" + str(text))
    print('\n')
    
    swap_or_replace = 0
    while swap_or_replace != 3:
        swap_or_replace = int(input("Would you like to swap or revert a letter? '1' to swap, '2' to revert, '3' to stop."))
        if swap_or_replace == 1:
            ct_letter = str(input("Input a ciphertext letter to replace (in uppercase)."))
            pt_letter = str(input("Input a plaintext letter that will replace the ciphertext letter (in lowercase)."))
            swapping = swapLetters(ct_letter, pt_letter, text)
            text = swapping
            print(text)

        elif swap_or_replace == 2:
            pt_letter = str(input("Input the plaintext letter that you would like to revert (in lowercase)."))
            ct_letter = str(input("Input the original ciphertext letter(in uppercase)."))
            revert = resetLetters(pt_letter, text, ct_letter)
            text = revert
            print(revert)
        
    return text

def sampletext(text):
    text = text.replace(" ", "")
    substring = []

    # for every char, go through every subsequent chars
    for i in range(len(text)):
        for j in range(i, len(text)):
            # printing substring in range i to j

            if len(text[i : j+1]) != 1:
                substring.append(text[i : j+1])

    return substring

def IC(text):   # Return Index Coincidence
    alphabet = sm.ascii_lowercase
    index_coincidence = 0

    for i in range(25):
        index_coincidence = text.count(alphabet[i]) * (text.count(alphabet[i]) - 1) + index_coincidence
        i += 1
    index_coincidence = index_coincidence * 1 / (len(text) * ((len(text))-1))
    
    return index_coincidence

def find_avg_keylength(substring):    # Return Avg. Index Coincidence of All Substrings
    new_list = []

    for i in range(len(substring)-1):
        new_list.append(IC(substring[i]))
    average_IC = (sum(new_list)) / len(substring)

    return average_IC

def find_vigenere_kl(average_IC):   # NEEDS DEBUGGING!

    freqEng = {'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40, \
    'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51, \
    'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28, \
    'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}

    closest = 10

    for i in range(25):
        if abs(freqEng[i] - average_IC) < closest:
            closest = freqEng[i]

        elif freqEng[i] == round(average_IC, 2):
            closest = freqEng[i]
            break
        break

    return closest

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

def revDict(letters):   # Reverse Dictionary for Decryption
    dictRev = {}

    # Reverse the keys and values in the dictionary
    for key in letters:
        dictRev[letters[key].upper()] = key.lower()
    return dictRev

def brute_force(text):  # Using Brute Force for Caesar Decryption
    possible = []

    # Using 25 reverse dictionaries that output possibilities
    for i in range(25):
        temp = masc(text, revDict(genCaesarAlpha(i)))
        possible.append(temp)

    return possible

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

def main(): # Main Shell for Function

    # Asking which MASC cipher to use
    choice = int(input("What would you like to do?\n[1] Encrypt with Caesar\n[2] Decrypt Caesar (knowing shift)\n[3] Break Caesar using brute force\n[4] Decrypt Caesar Using Chi-Squared Test\n[5] Encrypt with Keyword\n[6] Decrypt with Keyword\n[7] Frequency Analysis by Letter\n[8] Frequency Analysis in Descending Order\n[9] Show Histogram of Frequency\n[10] Print Top 10 Digraphs\n[11] Print Top 10 Trigraphs\n[12] Show Top 5 Double Letters\n[13] Cryptoanalysis Using Frequency Analysis\n[14] Index Coincidence\n"))
    text = ""

    if choice == 1: # Encrypt with Caesar
        text = str(input("Input the plaintext here."))
        k = int(input("Input the shift."))
        alpha = genCaesarAlpha(k)
        finalText = masc(text.lower(), alpha).upper()

    elif choice == 2: # Decrypt with Caesar
        text = str(input("Input the ciphertext here."))
        k = int(input("Input the shift. Negative for decryption."))
        alpha = genCaesarAlpha(k)
        finalText = masc(text.lower(), alpha).lower()

    elif choice == 3: # Brute Force Caesar
        k = int(input("Input the shift if applicable. Enter '0' if not applicable."))
        text = str(input("Input the encrypted text here.")).upper()
        finalText = ''

        alpha = genCaesarAlpha(k)
        finalText = masc(text.upper(), revDict(genCaesarAlpha(k)))

        for option in brute_force(text):
            finalText += option + '\n\n'

    elif choice == 4: # Find Caesar Shift + Decrypt with Chi-Squared Test
        text = str(input("Input the ciphertext here.")).upper()
        finalText = find_caesar_shift(text)

    elif choice == 5: # Encrypt with Keyword
        keyword = str(input("Input a keyword or keyphrase."))
        text = str(input("Input the plaintext here."))
        alpha = gen_kwd_dict(keyword)
        finalText = masc(text.lower(), alpha).upper()

    elif choice == 6: # Decrypt with Keyword
        keyword = str(input("Input a keyword or keyphrase."))
        text = str(input("Input the ciphertext here."))
        alpha = gen_kwd_dict(keyword)
        finalText = masc(text.upper(), revDict(gen_kwd_dict(keyword)))

    elif choice == 7:   # Show Frequencies in #'s and %'s
        text = str(input("Input the text here."))
        count_vs_percent = int(input("Would you like to see the number of occurences or the percentage frequency? '1' for # in dict format, '2' for # in histogram, '3' for '%' in alphabetical order."))
        finalText = letterFreqAlpha(count_vs_percent, text)

    elif choice == 8:   # Show Frequencies in %'s in Decreasing Order
        text = str(input("Input the text here."))
        count_vs_percent = 4
        finalText = printLetterFreqDecrease(letterFreqAlpha(count_vs_percent, text))

    elif choice == 9:   # Create Histogram / Bar Chart
        text = str(input("Input the text here."))
        count_vs_percent = 4
        finalText = histogram(letterFreqAlpha(count_vs_percent, text))

    elif choice == 10:   # Show Top 10 Digraphs
        text = str(input("Input the text here."))
        finalText = printDigraph(text)

    elif choice == 11:  # Show Top 10 Trigraphs
        text = str(input("Input the text here."))
        finalText = printTrigraph

    elif choice == 12:  # Show Top 5 Double Letters
        text = str(input("Input the text here."))
        finalText = doubleLetters(text)

    elif choice == 13:  # Use Frequency Analysis
        text = str(input("Input the text here.\n"))
        print('\n')
        digraph = printDigraph(text)
        trigraph = printTrigraph(text)
        doubles = doubleLetters(text)
        count_vs_percent = 4
        frequency = printLetterFreqDecrease(letterFreqAlpha(count_vs_percent, text))
        
        finalText = frequencyAnalysis(text, digraph, trigraph, doubles, frequency)

    elif choice == 14:  #Show Index of Coincidence
        text = str(input("Input the text here.\n"))
        finalText = IC(text)

    # Ask about how to give output text
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

print(main())   # Run Main Function to do All Operations
