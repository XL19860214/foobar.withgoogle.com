# Copyright (c) Xuwei Li

def solution(s):
    _dict = getDict()
    result = ''
    for char in s:
        if char.isupper():
            result += _dict['^'] + _dict[char.lower()]
        else:
            result += _dict[char]
    return result

# Construct a dictionary from sample data
def getDict():
    codeSpace = '000000'
    codeCapital = '000001'
    input = 'The quick brown fox jumps over the lazy dog'
    sample = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
    _dict = dict()
    _dict[' '] = codeSpace
    _dict['^'] = codeCapital
    result = sample
    for char in input:
        if char.isupper():
            _dict[char.lower()] = result[6:12]
            result = result[12:]
        else:
            _dict[char] = result[:6]
            result = result[6:]
    return _dict
