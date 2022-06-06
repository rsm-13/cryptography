import string
alphabet = string.ascii_lowercase

#Rotors (List of Shifts)
rIII = [1, 2, 3, 4, 5, 6, 22, 8, 9, 10, 13, 10, 13, \
        0, 10, 15, 18, 5, 14, 7, 16, 17, 24, 21, 18, 15]

rII =  [0, 8, 1, 7, 14, 3, 11, 13, 15, 18, 1, 22, 10, \
        6, 24, 13, 0, 15, 7, 20, 21, 3, 9, 24, 16, 5]

rI =   [4, 9, 10, 2, 7, 1, 23, 9, 13, 16, 3, 8, 2, \
        9, 10, 18, 7, 3, 0, 22, 6, 13, 5, 20, 4, 10]

#Reflector (Pairs in Dict)
reflB = {"a":"y", "b":"r", "c":"u", "d":"h", "e":"q", "f":"s", \
         "g":"l", "h":"d", "i":"p", "j":"x", "k":"n", "l":"g", \
         "m":"o", "n":"k", "o":"m", "p":"i", "q":"e", "r":"b", "s":"f", \
         "t":"z", "u":"c", "v":"w", "w":"v", "x":"j", "y":"a", "z":"t" }

#Starting Rotor Indeces & Rotor Notch Indeces (List, rIII: index 2, rI: index 0)
starting_pos = ['d','e','f']
notch_setup = ['q','e','v']

def shift_rotor(rotor):
    #Shift Rotor
    #Takes first index of rotor list and return that element

    rotor.append(rotor.pop(0))
    return

def encrypt_shift(char, rotor):
    #Returning the letter shifted by the index on the rotor (AKA encrypting)
    shifted = alphabet[(alphabet.index(char) + rotor[alphabet.index(char)]) % 26]
    return shifted

def revRotor(rotor):
    #Returns new list of all reverse shifts corresponding to original rotor shifts

    revRotor = [0] * 26

    for i in range(26):
        revRotor[(i + rotor[i]) % 26] = -1 * rotor[i]

    return revRotor

def plugboard(plug_config):
    plugbrd = {}

    #Create a dict key-value pair of the two chars in the pair
    for pair in plug_config:
        plugbrd[pair[0]] = pair[1]
        plugbrd[pair[1]] = pair[0]

    #For all remaining letters in alphabet not in plugbrd input, assign them to each other in dict
    for char in alphabet:
        if char not in plugbrd.keys():
            plugbrd[char] = char

    #Plugboard is a dict of all pairs
    return plugbrd

def starting_positions():
    #Shift rotor the number of times it takes to get to starting position
    
    #Third (fast) rotor starting position
    thrd_r = alphabet.index(starting_pos[2])
    for i in range(thrd_r):
        shift_rotor(rIII)
    
    #Second (med) rotor starting position
    sec_r = alphabet.index(starting_pos[1])
    for i in range(sec_r):
        shift_rotor(rII)
    
    #First (slow) rotor starting position
    fst_r = alphabet.index(starting_pos[0])
    for i in range(fst_r):
        shift_rotor(rI)

    return ''

def main():
    #Ask for plaintext in string, Set empty string for ciphertext
    pt = str(input("Input the plaintext here."))
    ct = ''

    #Set up plugboard pairs through taking input, then splitting into a list of pairs
    plug_config = str(input("Input the plugboard configuration, letter pairs separated by a space."))
    plug_config = plug_config.split(' ')

    #Take in new starting positions of rotors
    starting_positions()

    #Create counters to track number of times looped
    count1 = 0
    count2 = 0
    count3 = 0
    
    for char in pt:

        #Notch kicks in to make rII shift
        #When the first count is equal to the starting index of rIII minus the notch index of rIII
        #The second counter increases by 1
        if (count1 % 26) == abs(alphabet.index(starting_pos[2]) - alphabet.index(notch_setup[2])):
            shift_rotor(rII)
            count2 = (count2 + 1) % 26

            #Notch kicks in to make rII AND rI shift
            #When the second count mod 26 is equal to the starting index of rII minus the notch index of rII
            #The second and third counters increase by 1
            if (count2 % 26) == abs(alphabet.index(starting_pos[1]) - alphabet.index(notch_setup[1])):
                shift_rotor(rII)
                shift_rotor(rI)
                count2 = (count2 + 1) % 26
                count3 += 1

        #Go through encryption process (shift, plugbrd, rIII, rII, rI, reflB, rev(rI), rev(rII), rev(rIII), plugbrd)

        shift_rotor(rIII)
        count1 += 1

        plugged = plugboard(plug_config)[char]
        encrypted = encrypt_shift(plugged, rIII)
        encrypted = encrypt_shift(encrypted, rII)
        encrypted = encrypt_shift(encrypted, rI)
        encrypted = reflB[encrypted]
        encrypted = encrypt_shift(encrypted, revRotor(rI))
        encrypted = encrypt_shift(encrypted, revRotor(rII))
        encrypted = encrypt_shift(encrypted, revRotor(rIII))
        encrypted = plugboard(plug_config)[encrypted]
        ct += encrypted

    #Return ciphertext

    print('\n' + ct.upper())
    return ''

print(main())