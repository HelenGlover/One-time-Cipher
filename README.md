## One-time Pad Cipher
A simple program that allows the user to decipher and encipher a message

### Background:
Caesar cipher is a special encryption technique where each letter is replaced by another located a little further in the alphabet. This cipher can also use ascii code to disguise each letter as a number.

Cipher.py has a similiar format to the caesar cipher but it uses a stronger form of encryption called the one-time pad. This pad generates a random sequence of uppercase letters. It can only be deciphered if the receiver is given the shared-key from the sender to unshift each letter.

### Functions and how it works:
This program is composed of four major functions

shiftLetter
generatePad
encipher
decipher
A. shiftLetter: Shift a letter by a specified amount. Letters are shifted in accordance with its associated ascii code.

B. generatePad: Takes in a length of characters and uses that length to create a pad of random uppercase letters

B. encipher: Encrypts a message from the sender with the pad

C. decipher: Deciphers the provided encrypted-message.txt with the pad (Its a message about WWII code breakers!)
