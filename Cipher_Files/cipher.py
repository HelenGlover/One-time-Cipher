#This python code is performing an encryption of a message in ciphertext

#This code was referenced from the Cesear Cipher
import string

import random
from cipher_test import * 

#Reference from Cesear cipher
def shiftLetter(char,shift):
  ascii = ord(char)

  if (ascii >= 65) and (ascii <= 90): #uppercase characters compared to ascii
    shifted = (ascii - 65 + shift) % 26 + 65
  elif (ascii >= 97) and (ascii <= 122):
    shifted = (ascii - 97 + shift) % 26 + 97 # lowercase characters compared to ascii
  else:
    shifted = ascii

  return chr(shifted)

#generatePad function - onetime pad of random uppercase letters
def generatePad(len):
  one_pad = []
  for x in range (0, len):
    random_letters = ''.join(random.choice(string.ascii_uppercase)) # random string using random.choice function
    one_pad.append(random_letters()) # attach to the one_pad
  return "".join(one_pad)

#create a encipher message by shifting letters
def encipher(one_pad, message):
  index = 0
  new_code = [] 
  for i in range(len(message)): 
    ascii = ord(message[i])

    if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <= 122)):
      encipher_code = shiftLetter(message[i], ord(one_pad[index])-65)
      new_code.append(encipher_code)
      index += 1
    else:
      encipher_code = message[i]
      new_code.append(encipher_code)

  return "".join(new_code)

# create a decipher message by appending over the characters
def decipher(one_pad, message):
  new_code = []
  index = 0
  for i in range(0,len(message)):
    ascii = ord(message[i])
    if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <= 122)):
      encipher_code = shiftLetter(message[i], -ord(one_pad[index])-65)
      new_code.append(encipher_code)
      index += 1
    else:
      encipher_code = message[i]
      new_code.append(encipher_code)
      
  return "".join(new_code)

# open and read the message file
with open("encrypted-message.txt") as file:
  text = file.read()
with open("pad.txt") as file2:
  text2 = file2.read()
  print(decipher(text2, text))
