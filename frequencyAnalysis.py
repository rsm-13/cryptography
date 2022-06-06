from random import choice
import string as sm

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

def printLetterFreqAlpha(count_vs_percent, text):
    alphabet = [char for char in sm.ascii_lowercase]
    text = text.lower()
    frequency_num = {}
    frequency_percent = {}

    for char in text:
        if char in sm.whitespace:
            text = text.replace(char,'')
        elif char in sm.punctuation:
            text = text.replace(char,'')
    totalLength = len(text)

    for i in range(25):
        index = alphabet[i]
        occurrence = text.count(index)
        frequency_num[index] = occurrence
        frequency_percent[index] = (occurrence / totalLength) * 100

    if count_vs_percent == 1:
        return frequency_num

    else:
        for key in frequency_percent.keys():
            print(key + '\t' + str(round(frequency_percent[key], 1)) + '%')

def printLetterFreqDecrease(frequency_percent):
    # Sort the values
    sorted_values_descending = sorted(frequency_percent.values(), reverse = True)
    sorted_dict = {}
    frequency = ''

    for i in sorted_values_descending:
        for key in frequency_percent.keys():
            if frequency_percent[key] == i:
                sorted_dict[key] = frequency_percent[key]

    for key in sorted_dict.keys():
        print(key + '\t' + str(round(sorted_dict[key], 1)) + '%')

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

def main():
    choice = int(input("What would you like to do?\n[1] Frequency Analysis by Letter\n[2] Frequency Analysis in Descending Order\n[3] Test Decrypting Using Frequency Analysis\n"))
    
    if choice == 1:
        text = str(input("Input the text here."))
        count_vs_percent = int(input("Would you like to see the number of occurences or the percentage frequency? '1' for # and '2' for %."))
        finalText = letterFreqAlpha(count_vs_percent, text)

    elif choice == 2:
        text = str(input("Input the text here."))
        count_vs_percent = 3
        finalText = printLetterFreqDecrease(letterFreqAlpha(count_vs_percent, text))

    elif choice == 3:  # Use Frequency Analysis
        text = str(input("Input the text here.\n"))
        print('\n')
        digraph = printDigraph(text)
        trigraph = printTrigraph(text)
        doubles = doubleLetters(text)
        count_vs_percent = 4
        frequency = printLetterFreqDecrease(letterFreqAlpha(count_vs_percent, text))
        
        finalText = frequencyAnalysis(text, digraph, trigraph, doubles, frequency)

    return finalText

print(main())
