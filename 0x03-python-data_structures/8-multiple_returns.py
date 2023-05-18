#!/usr/bin/python3
# more returns

def multiple_returns(sentence):
    for i in sentence:
        if i == sentence[0]:
            break
    length = len(sentence)
    return length, i
