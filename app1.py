import difflib
from difflib import SequenceMatcher

def compare(x, y):
    x = x.lower()
    y = y.lower()
    return SequenceMatcher(None, x, y).ratio()

#example
print(compare("sandwich", "samwich"))