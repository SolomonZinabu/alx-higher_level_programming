#!/usr/bin/python3
<<<<<<< HEAD


def multiple_returns(sentence):
    """Returns tuple with len of string and first char"""
    length = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return (length, first)
=======
def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, None
    else:
        return len(sentence), sentence[0]
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
