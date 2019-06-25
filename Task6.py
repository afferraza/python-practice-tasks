"""
Write a program that accepts a sentence and calculate the number of letters and digits.
"""

def count(sentence):
    letters= 0
    digits = 0
    for x in sentence:
        if x.isdigit():
            digits += 1

        if x.isalpha():
            letters += 1
    print("Letters : %d"%letters)
    print("Digits : %d"%digits)

count("AfferRaza123")