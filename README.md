# Cryptography / Ciphers
Cryptography &amp; Cipher Algorithms for Encryption &amp; Decryption

## **Overview**
This project involved experimentation with various cryptographical encryption and decryption methods. Starting with medieval techniques with the Caesar cipher and Vigenère cipher, different algorithms were created for encrypting plaintext with these ciphers as well as writing programs to break them using statistical analysis with the chi-square test or Kasiski method. Other monoalphabetic substitution-related functions were created and can be viewed in ```mascMasterCode.py```. Repo includes a frequency analysis algorithm, a famous monoalphabetic substitution codebreaking technique created by cryptanalyst al-Kindī in 19th Century Arabia. Other files include a mock-up of an enigma machine (famously used during WWII), a version of the OTP cipher (one-time pass, also known as the vernam cipher), and a basic RSA algorithm which implements the modern idea of public-key cryptography in internet security.

## **Files**

- ```Evolution of Ancient and Medieval Ciphers [Research Paper].pdf```
  * Wrote a research paper about the evolution of ancient and medieval ciphers – specifically with regards ancient European and Arabic cryptographic methods.
- ```ADFGVX_cipher.py```
  * A transposition field-cipher used during WWI by the Imperial German Army. The cipher is given its named after the fact that 'ADFGVX' are the only letters which appear in the ciphertext. The program completes basic encryption via the polybius square and then converts it into morse code for a second layer of protection.
- ```caesarCipher.py```
  * Very basic caesar cipher encryption / decryption tool (if shift is known). If shift is unknown, brute-force technique can be implemented, providing 26 outputs, each with a different caesar shift.
- ```caesarMasc.py```
  * More complex / efficient caesar cipher program. Uses modular arithmetic and dictionaries as opposed to lists for encryption. File can find a caesar shift for decryption using the chi-square test. Also contains all of the functions in ```caesarCipher.py```
- ```enigmaMachine.py```
  * File creates a mock-up of an enigmaMachine for encryption. Plugboard is set via a dictionary and rotor initial positions can be set. Enigma machines were famously used during WWII. They were effective as the inital plaintext letter would undergo encryption between 7-9 times, but the USA ultimately found a way to decode the messages.
- ```frequencyAnalysis.py```
  * The frequency analysis program (method invented in 19th century Arabia by cryptanalyst, al-Kindī) shows frequencies of a ciphertext in both percentages and occurrences, the top 10 digraphs, the top 10 trigraphs, and the top 5 double letter occurrences. It also allow the user to perform decryption of a monalphabetic substitution through altering letters using the data.
- ```keywordCipher.py```
  * Performs encryption for a cipher whose substitution dictionary is dependent on a specific keyword. Keyword is necessary for decryption.
- ```mascMasterCode.py```
  * Contains most monoalphabetic substitution techniques (includes repeats of other files). Includes: caesar cipher functions, chi-square test, frequency analysis, and keyword cipher.
- ```numberTheory.py```
  * Simple prime number functions. (checking if a number is prime, prime factorization, checking if two nums are co-prime, finding the phi value of a number)
- ```OTP_cipher.py```
  * One-time-pass cipher, also known as the vernam cipher. Uses the Baudot code to encode the text and figs and then encrypts the code through XOR (eXclusive-or). If the key is known, decryption can also be performed.
- ```rsa_algorithm.py```
  * Basic RSA algorithm encryption/decryption (used in internet security with public-key cryptography). Implements modular arithmetic. Can be used for smaller primes (usually less than 1000). For decryption, private-key must be known. ```e = 65537```
- ```vigenereCipher.py```
  * Medieval polyalphabetic substitution cipher. Recognized as *le chiffre indechiffrable*, or 'the indecipherable cipher'. Uses a keyword for encryption according to the Tabula Recta. Decryption can be performed with keyword, and Kasiski method is implemented if the keyword and keylength are both unknown.
