# coding: utf-8
# python 3.7 x86_64

import sys
import getopt

alpha_b64 = {}


def main(argv) -> None:
    try:
        opts, arg = getopt.getopt(argv, "e:d:", [])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-d":
            print(f"decode {str(arg)}")
        elif opt == "-e":
            print(b64_encode(arg.encode('utf-8')))

def b64_encode(string:bytes) -> str:
    binary = ''.join([bin(c).split('b')[-1] for c in string])
    print(binary)
    while len(binary) % 6 != 0:
        binary += '0'
    print(binary)
    return f"encode {string.decode('utf-8')}"


if __name__ == "__main__":
    main(sys.argv[1:])
