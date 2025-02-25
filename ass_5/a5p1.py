#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2025 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 5 Problem 1 Student Solution
January 2025
Author: <Your name here>
"""
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)

def freqDict(ciphertext: str) -> dict:
    """
    Analyze the frequency of the letters
    """
    # Count letter frequencies in ciphertext (ignoring non-alpha characters)
    letter_counts = Counter(c for c in ciphertext if c.isalpha())
    
    # Sort by frequency (descending), then by alphabetical order (ascending)
    sorted_letters = sorted(letter_counts.keys(), key=lambda c: (-letter_counts[c], c))
    
    # Map sorted letters to ETAOIN frequency order
    mapping = {cipher: plain for cipher, plain in zip(sorted_letters, ETAOIN)}
    
    return mapping


def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """
    return ''.join(mapping.get(c, c) for c in ciphertext)

def test():
    "Run tests"
    assert type(freqDict("A")) is dict
    assert freqDict("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")["A"] == "E"
    assert freqDict("AABBA")['B'] == "T"
    assert freqDict("-: AB CD AH")['A'] == "E"
    assert freqDecrypt({"A": "E", "Z": "L", "T": "H", "F": "O", "U": "W", "I": "R", "Q": "D"}, "TAZZF UFIZQ!") == "HELLO WORLD!"


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
