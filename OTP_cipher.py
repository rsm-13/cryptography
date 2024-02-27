#Baudot Code

#Dictionaries Containing Pt to Baudot Assignments (Ltrs & Figs)
baudot_alpha = {'<':'11111','E':'00001',' ':'00100','\n':'00010','A':'00011','S':'00101','I':'00110','U':'00111','D':'01001','R':'01010','J':'01011',\
'N':'01100','F':'01101','C':'01110','K':'01111','T':'10000','Z':'10001','L':'10010','W':'10011','H':'10100',\
'Y':'10101','P':'10110','Q':'10111','O':'11000','B':'11001','G':'11010','M':'11100','X':'11101','V':'11110',}

baudot_figs = {'>':'11011','@':'00000','3':'00001','-':'00011',' ':'00100',"'":'00101','\n':'00010','8':'00110','7':'00111','4':'01010', \
',':'01100','!':'01101',':':'01110','(':'01111','5':'10000','+':'10001',')':'10010','2':'10011','$':'10100',\
'6':'10101','0':'10110','1':'10111','9':'11000','?':'11001','&':'11010','.':'11100','/':'11101',';':'11110'}

def uploadFile(file):   #Upload a File
    newString = ""
    with open (file) as f:
        lines = f.readlines()

        for i in lines:
            newString += i

    return newString

def revDict(baudot_stuff):   #Reverse Dictionary for Decryption
    dictRev = {}

    #Reverse the keys and values in the dictionary
    for key in baudot_stuff:
        dictRev[baudot_stuff[key].upper()] = key.lower()
    return dictRev

def encode_pt(text):    #Encoding the pt with Baudot
    text = text.upper()
    text.split(' ')
    encoded = ''

    for i in range(len(text)):
        #Define pt chars if letters or figs
        if str(text[i:i+4]) == 'LTRS':
            text = text.replace(text[i:i+4], '<')

        elif str(text[i:i+4]) == 'FIGS':
            text = text.replace(text[i:i+4], '>')
    
    for char in text:
        #Encoding with Baudot based on the Char Type
        if char in baudot_alpha:
            char = baudot_alpha[char]

        elif char in baudot_figs:
            char = baudot_figs[char]

        encoded += (char)
    print(encoded)
    return ('' + str(encoded))

def crypt_baud(encoded,keystream):  #Encrypting the Encoded Bits with Vernam
    #Creating Empty String for Encrypted Text
    #Converting the text and key into a string
    crypted = ''
    string_text = str(encoded)
    string_key = str(keystream)

    #Going through all of the bits from encoded text and doing XOR
    i = 0
    while i < len(str(encoded)):
        crypted += str(int(string_text[i]) ^ int(string_key[i]))
        i += 1

    print(crypted)
    return crypted

def alpha(bits):    #Decrypting Letters
    #Using reverse dictionary to find 5 bit string to letter assignment
    rev = revDict(baudot_alpha)
    new = rev[bits]
    return new

def figs(bits): #Decrypting Figures
    #Using reverse dictionary to find 5 bit string to fig assignment
    rev = revDict(baudot_figs)
    new = rev[bits]
    return new

def decrypt_baud(text,keystream):   #Decrypting Vernam
    #Doing XOR on vernam text to get encoded text
    crypted = crypt_baud(text,keystream)

    i = 0
    pt = ''
    ltrs = False

    while i < len(crypted):

        #Going through each 5 bit string and defining whether the following bits will be ltrs or figs
        if str(crypted[i:i+5]) == '11111':
            ltrs = True

        elif str(crypted[i:i+5]) == '11011':
            ltrs = False

        #Using the char type, decrypt using the alpha and figs function
        if ltrs == True:
            char = alpha(crypted[i:i+5])
            pt += char

        else:
            char = figs(crypted[i:i+5])
            pt += char

        i += 5  #Loop through next 5 bit string

    p = 0
    while p < len(pt):
        #Replacing the 'ltrs' and 'figs' indicators
        if pt[p] == '<': 
            current = pt[p]
            pt = pt.replace(current, '')

        if pt[p] == '>':
            current = pt[p]
            pt = pt.replace(current, '')
            
        p += 1

    print(pt)

def main(): #Vernam Main
    #Asking whether to encrypt or decrypt & uploading "random" key
    choice = int(input('Would you like to encrypt & send a message, or decrypt a received file?\n[1] encrypt\n[2] decrypt\n'))
    #key = uploadFile(filepath)
    key = '100101010000001011111001000000000100101010000001011111001000000000100101010000001011111001000000000100101010000001011111001000000000100101010000001011111001000000000'

    if choice == 1: # Encrypt with Vernam
        text = str(input('Message must begin with either "LTRS" for letters or "FIGS" for other chars. Indicate the switch of char type. Input message here.'))
        final = crypt_baud(encode_pt(text),key)
        
    elif choice == 2: # Decrypt
        #text = uploadFile(filepath)
        text = str(input("Input the encrypted bits here. Use only 0\'s and 1\'s and no spaces."))
        final = decrypt_baud(text,key)
    
    return final

main()
