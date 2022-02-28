#This python code is performing an encryption of a message

#This code was referenced from the Cesear Cipher
import string
from random import random

#Reference from Cesear cipher
def shiftLetter(char,shift):
  ascii = ord(char)

  if (ascii >= 65) and (ascii <= 90): #ascii uppercase characters
    shifted = (ascii - 65 + shift) % 26 + 65
  elif (ascii >= 97) and (ascii <= 122):
    shifted = (ascii - 97 + shift) % 26 + 97 # ascii lowercase charactrs 
  else:
    shifted = ascii

  return chr(shifted)

#generatePad function - onetime pad of random uppercase letters
def generatePad(len):
  one_pad = []
  for x in range (0, len):
    random_letters = ''.join((random.choice(string.ascii_uppercase)))
    one_pad.append(random_letters())
  return "".join(one_pad)

#crate a encipher message by shifting letters
def encipher(one_pad, message):
  index = 0
  new_code = [] 
  for i in range(len(message)):  #loop over the length of the message
    ascii = ord(message[i])
    if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <= 122)): # if letters is in these ascii areas
      encipher_code = shiftLetter(message[i], ord(one_pad[index])-65)
      new_code.append(encipher_code) # attach encipher with empty new code list
      index += 1
    else:
      encipher_code = message[i]
      new_code.append(encipher_code)

  return "".join(new_code)

# create a decipher message by appending over the characters
def decipher(one_pad, message):
  new_code = []
  index = 0
  for i in range(0,len(message)): #loop over the length of the message
    ascii = ord(message[i])
    if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <= 122)):  # if letters is in these ascii areas
      encipher_code = shiftLetter(message[i], -ord(one_pad[index])-65)
      new_code.append(encipher_code) # attach decipher with empty new code list
      index += 1
    else:
      encipher_code = message[i]
      new_code.append(encipher_code)
      
  return "".join(new_code)

# open and read the encrypted message and pad 
with open("encrypted-message.txt") as file:
  text = file.read()
with open("pad.txt") as file2:
  text2 = file2.read()
  print(decipher(text2, text)) # decipher random letter pad with message