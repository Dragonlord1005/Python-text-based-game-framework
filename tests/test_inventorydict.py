# This is the dictionary version of the inventory system, read the class version for more info
def returnprint(x):
    return x


def test_returnprint():
    if returnprint("hi") != "hi":
        raise AssertionError