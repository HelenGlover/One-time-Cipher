#  **One-time Pad Cipher**

*A simple program that allows the user to decipher and encipher a message*


## Background: 
*Caesar cipher* is a special encryption technique where each letter is replaced by another located a little further in the alphabet. This cipher can also use ascii code to disguise each letter as a number. 

`Cipher.py` has a similiar format to the caesar cipher but it uses a stronger form of encryption called the *one-time pad*. This pad generates a random sequence of uppercase letters. It can only be deciphered if the receiver is given the shared-key from the sender to unshift each letter.
 
 
## Functions and how it works: 
This program is composed of four major functions
- `shiftLetter`
- `generatePad`
- `encipher`
- `decipher`

> A. `shiftLetter`: Shift a letter by a specified amount. Letters are shifted in accordance with its associated [ascii code](https://www.ascii-code.com/).

> B. `generatePad`: Takes in a length of characters and uses that length to create a pad of random uppercase letters
 
> B. `encipher`: Encrypts a message from the sender with the pad

> C. `decipher`: Deciphers the provided `encrypted-message.txt` with the pad (Its a message about WWII code breakers!)

## Creating Tests:

These functions are important as they make up the tests needed to check the functionality of individual parts of the code. They also anticipate the times where your code could potentially fail. There can be multiple tests for each function (as seen in `shiftLetter`)


Use the `assert` keyword to return each test as `True`. You can also "throw an exception"  in a if...else statement using the `raise` keyword.



## How to run tests:
To run your test, you can use the VS Code source editor.

**Steps:**

1. *Install pytest:* Write the `pip install pytest` command in your terminal. Make sure the `pytest` is the most recent version.
  
3. *Right files:* Make sure all the files are located in the same repository. Open them with VS Code.
  
4.  *Connect:* You now need to connect/import `cipher.py` with the `cipher_tests.py`. Write `from cipher_test import` at the top of `cipher.py`. 
    
5. *Run:* Go to your terminal and enter `pytest cipher_test.py`. Make sure that your terminal is in the correct repository or else it won't run.
    
6.  *Run tests:* If the code works, all the tests should pass. If not, the program will display the errors in red.

Congratulations if all tests pass!