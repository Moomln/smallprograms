import sys
from time import *

import random

def deck():
    deck = []
number = ["1", "2", "3","4" ,"5" ,"6" ,"7" ,"8", "9", "10", "J", "Q", "K"]
rank = ["h", "c", "s", "d"]
for r in rank:
    for n in number:
        deck.append(r+n)
return deck



print("Welcome to your personal poker probability calculator")