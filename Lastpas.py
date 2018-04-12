#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import string
import hjson # Still works with json but hjson is only used to test it and have comments in json objects
import pyperclip # Used for saving to clipboard
# You may get an error message that says: “Pyperclip could not find a copy/paste mechanism for your system. Please see https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error for how to fix this.”

with open("auth.hjson", "r", encoding='utf-8-sig') as jsonFile: #Get passfrase that will be used to generat a password
        data = hjson.load(jsonFile)

# https://technet.microsoft.com/en-us/library/cc786468(v=ws.10).aspx
# Uppercase characters of European languages (A through Z, with diacritic marks, Greek and Cyrillic characters)
# Lowercase characters of European languages (a through z, sharp-s, with diacritic marks, Greek and Cyrillic characters)
# Base 10 digits (0 through 9)
# Nonalphanumeric characters: ~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/

# https://docs.python.org/2/library/string.html
uppercase = string.ascii_uppercase # Only uppercase letters
lowercase = string.ascii_lowercase # Only lowercase letters
numeric = string.digits # numbers 0-9
nonalphanumeric = string.punctuation # special characters !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
normalcharacters = string.printable # Combination of digits, letters, punctuation, and whitespace.

key = "google" # The key value/name you want to generate the password from, This will be a input from terminal later (thats the plan)
passwordlength = 8 # Minimum password length needed to be 8 to make sure you get atleest 2 uppercase, lowercase, number and special character
generatedpassword = '' # Made do define generatedpassword as a string
devidedpassword = int(passwordlength/2) # Used to index when the diffrent characters should be used
multiplyer = int(data['asciimultiplyer']) # Get a int number that will be used to multiply to destort any patterns
paddingindex = (data['startindex']*multiplyer)%len(normalcharacters)

if len(key) < passwordlength: # add padding to the key so the password dont have any repetitions
    index = paddingindex
    while len(key) < passwordlength:
        key += normalcharacters[index]
        index +=1

for i in range(passwordlength):
    index = i%len(key) # The index that we want to use in the key and make sure the index is not larger the key len
    keyasciinumber = ord(key[index]) # The asciinumber for the letter we are on in the index in the key
    passfraseindex = keyasciinumber%len(data['passfrase']) # Get index to use to get a passfrace character and making sure the idex is not larger then passfrace len
    passfraseasciinumber = multiplyer*ord(data['passfrase'][passfraseindex]) # The asciinumber for the leter in passfrace that we got from passfraseasciinumber

    if i % devidedpassword == 0:
        passwordindex = passfraseasciinumber%len(uppercase) # Index for the password based on the length of the set of characters we want to pick
        passwordcharacter = uppercase[passwordindex] # Get the character that will be used in the password
    elif i % devidedpassword == 1:
        passwordindex = passfraseasciinumber%len(lowercase)
        passwordcharacter = lowercase[passwordindex]
    elif i % devidedpassword == 2:
        passwordindex = passfraseasciinumber%len(numeric)
        passwordcharacter = numeric[passwordindex]
    elif i % devidedpassword == 3:
        passwordindex = passfraseasciinumber%len(nonalphanumeric)
        passwordcharacter = nonalphanumeric[passwordindex]
    else:
        passwordindex = passfraseasciinumber%len(normalcharacters)
        passwordcharacter = normalcharacters[passwordindex]
    generatedpassword += passwordcharacter

print(generatedpassword)
print(len(generatedpassword))
pyperclip.copy(generatedpassword) # Saves the generated password to clipboard
