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
CMPUT 331 Assignment 5 Problem 2 Student Solution
January 2025
Author: <Your name here>
"""

from sys import flags
import numpy as np
from collections import Counter
def evalDecipherment(text1: str, text2: str):
    """
    text1 is a plaintext and text2 is an attempted decipherment of a
    ciphertext created by enciphering text1.

    This function should compare the two files and return a list containing two fields that
    correspond to the key accuracy and decipherment accuracy of text2 w.r.t. the plaintext, text1
    """

    correct_key_count = 0
    correct_decipherment_count = 0
    
    text1 = text1.lower()
    text2 = text2.lower()

    unique_chars = set(c for c in text1 if c.isalpha())

   
    for char in unique_chars:
        if char in text1 and char in text2:
            correct_key_count += 1

   
    for char1, char2 in zip(text1, text2):
        if char1.isalpha() and char2.isalpha() and char1 == char2:
            correct_decipherment_count += 1

   
    key_accuracy = correct_key_count / len(unique_chars) if unique_chars else 0
    decipherment_accuracy = correct_decipherment_count / sum(1 for c in text2 if c.isalpha())

    return [key_accuracy, decipherment_accuracy]



def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()
