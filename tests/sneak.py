# This is for sneaking
import random


def stealth():
    """Defines stealth"""
    sneak = random.randint(1, 10)
    if sneak == (1 or 2 or 3 or 4 or 5):
        print("You sneak past")
    elif sneak:
        print("You don't sneak past and are caught,")
        print("this does nothing in the example")