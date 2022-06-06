import string as sm

def caesar(text, k, e):                       					#Encrypt / Decrypt
	dict = {}
	ct = ''
	alphabet = sm.ascii_letters

	if e == True:
		for i in range(len(alphabet)):
			dict[alphabet[i]] = alphabet[(i + k) % 26].upper()

		for char in text:
			if char in sm.whitespace:
				ct += char

			elif char in sm.punctuation:
				continue

			else:
				ct += dict[char]

	if e == False:
		for i in range(len(alphabet)):
			dict[alphabet[i]] = alphabet[(i - k) % 26].upper()

		for char in text:
			if char in sm.whitespace:
				ct += char

			elif char in sm.punctuation:
				continue

			else:
				ct += dict[char]

	return ct                 								#Return cipher text

def brute_force_caesar(text):
	posBreak = []
	for i in range(26):
		temp = sm.ascii_lowercase[i:] + sm.ascii_lowercase[:i]
		newText = text.lower().translate(text.maketrans(temp, sm.ascii_lowercase))
		posBreak.append(newText)
	return posBreak

def main():                                       	#Main shell for running program
	e = None                                      	#Set e = None as it will change based on decision of encrypting/decrypting/brute-force

	e_or_d = int(input("Would you like to encrypt or decrypt with Caesar cipher? Enter '1' to encrypt and '2' to decrypt. If you'd like to break the code using brute-force, enter '3'."))
	k = int(input("Input the shift amount. Positive numbers will shift to the right and negative to the left."))
	print_or_file = int(input("Would you like to print the result or write it into a new file? Type '1' to print and '2' to file."))
	text = str(input("Enter the text here."))

	if e_or_d == 1:                               	#Use caesar_encrypt to encrypt the text
		e = True

	elif e_or_d == 2:                             	#Use caesar_decrypt to encrypt the text
		e = False

	elif e_or_d == 3:                             	#Use brute_force_caesar
		e = None

	if print_or_file == 1:                        	#Print the result
		if e == None:
			return '\n'.join(brute_force_caesar(text))

		else:
			return caesar(text, k, e)

	elif print_or_file == 2:                      	#File the result into 'cipher.txt'
		if e == None:
			with open("cipher.txt", 'w') as w:
				w.write("\n".join(brute_force_caesar(text)))
			return "It has been written into 'cipher.txt'"

		if e == 1 or e == 2:
			with open("cipher.txt", 'w') as w:
				w.write(caesar(text, k, e))
			return "It has been written into 'cipher.txt'"
	else:
		pass

print(main())
