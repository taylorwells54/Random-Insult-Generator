randominsult.py
from random import randint
print("""random insult generator!!!

self confidence is overated""")
def chooser(False):
    while chooser == False:
        insults = [
            "heck you",
            "poopy-pants",
            "you suck",
            "idiot",
            "your more orange than trump",
            "you smell like a skunk",
            "fart muncher",
            "butt munch",
            "big 🅱umper"
        ]
        choice = randint(0,len(insults))
        print insults[choice]
