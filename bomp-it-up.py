#!/bin/env python3
from bomp.core import *
from bomp.process import *
from sys import argv


def main():
    CODE = 91
    PROXY = {}
    DELAY = 1
    COUNT = 30
    THREAD = 5
    for i in range(len(argv)):
        if argv[i].startswith("-"):
            try:
                if argv[i] in CORE["LIST"]["ARGS"]:
                    if argv[i] in ("-c", "--code"):
                        CODE = argv[i+1]
                    elif argv[i] in ("-p", "--proxy"):
                        PROXY = argv[i+1]
                    elif argv[i] in ("-d", "--delay"):
                        DELAY = int(argv[i+1])
                    elif argv[i] in ("-v", "--victom"):
                        VICT = argv[i+1]
                    elif argv[i] in ("-m", "--message"):
                        COUNT = int(argv[i+1])
                    elif argv[i] in ("-t", "--thread"):
                        THREAD = int(argv[i+1])
                else:
                    print(CORE["HELP"]);return
            except:
                print(CORE["HELP"]);return
    if len(argv) == 1:
        print(CORE["HELP"]);return
    try:
        bomp(VICT, COUNT, THREAD, CODE, PROXY, DELAY)
    except:
        print(CORE["HELP"]);return

if __name__ == "__main__":
    main()

