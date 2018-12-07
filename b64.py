# coding: utf-8
# python 3.7 x86_64

import sys
import getopt

from collections import Counter

"""
    Very simple implementation of base64 encode/decode
"""
b64_bin_to_char = {
    "000000": "A", "010001": "R", "100010": "i", "110011": "z",
    "000001": "B", "010010": "S", "100011": "j", "110100": "0",
    "000010": "C", "010011": "T", "100100": "k", "110101": "1",
    "000011": "D", "010100": "U", "100101": "l", "110110": "2",
    "000100": "E", "010101": "V", "100110": "m", "110111": "3",
    "000101": "F", "010110": "W", "100111": "n", "111000": "4",
    "000110": "G", "010111": "X", "101000": "o", "111001": "5",
    "000111": "H", "011000": "Y", "101001": "p", "111010": "6",
    "001000": "I", "011001": "Z", "101010": "q", "111011": "7",
    "001001": "J", "011010": "a", "101011": "r", "111100": "8",
    "001010": "K", "011011": "b", "101100": "s", "111101": "9",
    "001011": "L", "011100": "c", "101101": "t", "111110": "+",
    "001100": "M", "011101": "d", "101110": "u", "111111": "/",
    "001101": "N", "011110": "e", "101111": "v",
    "001110": "O", "011111": "f", "110000": "w",
    "001111": "P", "100000": "g", "110001": "x",
    "010000": "Q", "100001": "h", "110010": "y"}

b64_char_to_bin = {val: key for key, val in b64_bin_to_char.items()}
complement = {0: '', 2: "=", 4: "=="}

def main(argv) -> None:
    try:
        opts, arg = getopt.getopt(argv, "e:d:", [])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-d":
            print(b64_decode(arg))
        elif opt == "-e":
            print(b64_encode(arg))

def b64_encode(string:str) -> str:
    binary = ''.join([f"{ord(c):08b}" for c in string])

    pad, binary = _padding(binary)
    print(binary)
    return _encode(binary, pad)

def _padding(string:str) -> tuple:
    i = 0
    while len(string) % 6 != 0:
        i += 1
        string += "0"
    return i, string

def _encode(binary:str, pad:int) -> str:

    string_b64 = ""
    while len(binary) != 0:
        binary_temp, binary = binary[:6], binary[6:]
        string_b64 += b64_bin_to_char.get(binary_temp)
    string_b64 += complement.get(pad)
    return string_b64

def b64_decode(string_b64:str) -> str:
    string_b64 = string_b64[:-Counter(string_b64)["="]]

    binary_b64 = "".join([b64_char_to_bin.get(c) for c in string_b64])

    return _decode(string_b64)

def _decode(binary_b64):
    string = ""
    # TODO
    return string

if __name__ == "__main__":
    main(sys.argv[1:])
