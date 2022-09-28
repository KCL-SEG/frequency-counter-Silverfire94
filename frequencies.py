"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item_ = str(item)
        if item_ in frequencies.keys():
            frequencies[item_] += 1
        else:
            frequencies[item_] = 1
    # Your code goes here
    return frequencies
