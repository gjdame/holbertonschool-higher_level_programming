#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        len_s = len(sentence)
        char = sentence[:1]
        return(len_s, char)
    else:
        sentence = None
        return(0, sentence)
