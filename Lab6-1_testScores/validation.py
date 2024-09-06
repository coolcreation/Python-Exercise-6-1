#!/usr/bin/env python3
# Jeff Bohn
# 9/5/2024
# Week_3_Lab_2 
# Chapter 6 - Lists & Tuples
# validation.py

"""
Args: User input needs to be int(), float(), or 'x'

Returns: User prompt if valid, else False
"""

def validate(prompt):
    if(prompt == 'x'):
        return prompt
    
    while True:
        try:
            prompt = float(prompt)
            if(prompt >= 0 and prompt <= 100):
               return prompt
            else:
                return False
        except:
            print("Error, numbers between 0-100 only. Try again!")
            return False
