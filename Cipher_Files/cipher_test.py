#This program runs multiple unit tests to determine if the code is working properly 
#Reference from week 4 cipher_test
from cipher import * 
from random import random

# These tests help determine if the shiftLetter function is working
def test_align_ascii(): #Test for letters with corresponding ascii
  assert shiftLetter("a", 0) =="a"

def test_forward(): #Test for shifting forward
  assert shiftLetter("a", 9) == "j"
    
def test_negative_backwards(): #Test for shifting backwards
  assert shiftLetter("a", -9) == "r" 

def test_shift_26(): #Test for shifting by 26 - alphabet
  assert shiftLetter("a", 26) == "a" 

def generatePad(): # Test for ensuring randomness in the pad
  generatePad(10) != generatePad(10)


def test_encipher_begin(): #Test for encrypted letters of As
  if encipher("ABC", "AAA") == "ABC": 
    assert True
  else:
    raise Exception("Error in the shifting of letters")

def test_encipher_end(): #Test for encrypted letters of Zs
  if encipher("ABC", "ZZZ") == "ZAB": 
    assert True
  else:
    raise Exception("Error in the shifting of letters")


def test_decipher_begin(): #Test for deciphering letters starting at A
  if decipher("ABC", "AAA") == "ABC": 
    assert True

def test_decipher_end(): #Test for deciphering letters starting at Z
  if decipher("ZAB", "ZZZ") == "ABC": 
    assert True

