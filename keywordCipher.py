import string as sm

def gen_kw_dict(keyword):
	alpha = {}
	alphabet = sm.ascii_lowercase

	for char in keyword:
		if char in sm.whitespace:
			keyword = keyword.replace(char, "")
		elif char in sm.punctuation:
			keyword = keyword.replace(char, "")

	keys = [char for char in alphabet]
	keys = list("".join(dict.fromkeys(alphabet)).lower())
	values = list("".join(dict.fromkeys(keyword)).upper())

	lastIndex = keyword[-1].lower()
	index = alphabet.index(lastIndex) + 1
	end_alphabet = alphabet[index:]
	beg_alphabet = alphabet[:index]

	for char in end_alphabet:
		values.append(char.upper())

	for char in beg_alphabet:
		values.append(char.upper())

	values = "".join(dict.fromkeys(values)).upper()
	alpha = dict(zip(keys, values))

	return alpha

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

def revDict(letters):
    dictRev = {}

    # Reverse the keys and values in the dictionary
    for key in letters:
        dictRev[letters[key].upper()] = key.lower()
    return dictRev

def main():
	choice = int(input("What would you like to do?\n[1] Encrypt with Keyword\n[2] Decrypt with Keyword\n"))
	text = ''

	if choice == 1: # Encrypt Keyword
		text = str(input("Input the plaintext here."))
		keyword = str(input("Input a keyword or keyphrase."))
		alpha = gen_kw_dict(keyword)
		finalText = masc(text.lower(), alpha).upper()

	elif choice == 2: # Decrypt with Keyword
		keyword = str(input("Input a keyword or keyphrase."))
		text = str(input("Input the ciphertext here."))
		alpha = gen_kw_dict(keyword)
		finalText = masc(text.upper(), revDict(gen_kw_dict(keyword)))

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
