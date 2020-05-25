#!/usr/bin/env python3

# Author: Christian Bargraser

import os
import sys
import argparse
import crypher.ceasar as cea
import crypher.cryparse as cyp

parser = argparse.ArgumentParser()
cyp.addCipherArgs(parser)

group_shift = parser.add_mutually_exclusive_group(required=True)
group_shift.add_argument('-s', '--shift', type=int, help='number of times to shift letter (absolute value will be used)')
group_shift.add_argument('-b', '--bruteforce', action='store_true', help='try all combinations')

dictArgs = vars(parser.parse_args())

if None != dictArgs.get('input') and not os.path.isfile(dictArgs.get('input')):
    print('No such file:', dictArgs.get('input'), '\n')
    parser.print_help()
    sys.exit(1)

cipher = cea.CeasarCoder(dictArgs.get('shift'))

# not bruceforce
if False == dictArgs.get('bruteforce'):

    if cyp.isEncodeStr(dictArgs):
        print(cipher.encodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))

    elif cyp.isEncodeFile(dictArgs):
        print(cipher.encodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))

    elif cyp.isDecodeStr(dictArgs):
        print(cipher.decodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))
    
    else:
        print(cipher.decodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))

# bruteforce
else:

    coder.bPrintShift = True

    if cyp.isEncodeStr(dictArgs):
        for i in range(0, len(cipher.strAlphaM)):
            cipher.iShift = i
            print(cipher.encodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))
    
    elif cyp.isEncodeFile(dictArgs):
        for i in range(0, len(cipher.strAlphaM)):
            cipher.iShift = i
            print(cipher.encodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))

    elif cyp.isDecodeStr(dictArgs):
        for i in range(0, len(cipher.strAlphaM)):
            cipher.iShift = i
            print(cipher.decodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))

    else:
        for i in range(0, len(cipher.strAlphaM)):
            cipher.iShift = i
            print(cipher.decodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))
