#!/usr/bin/env python3

# Author: Christian Bargraser

import os
import sys
import argparse
import crypher.vigenere as vig
import crypher.cryparse as cyp

parser = argparse.ArgumentParser()
cyp.addCipherArgs(parser)

parser.add_argument('-k', '--key', help='plaintext file', required=True)

dictArgs = vars(parser.parse_args())

if None != dictArgs.get('input') and not os.path.isfile(dictArgs.get('input')):
    print('No such file:', dictArgs.get('input'), '\n')
    parser.print_help()
    sys.exit(1)

coder = vig.VigenereCoder()

if cyp.isEncodeStr(dictArgs):
    print(coder.encodeStr(dictArgs.get('text'), dictArgs.get('key'), strOutputFile=dictArgs.get('output')))

elif cyp.isEncodeFile(dictArgs):
    print(coder.encodeFile(dictArgs.get('input'), dictArgs.get('key'), strOutputFile=dictArgs.get('output')))

elif cyp.isDecodeStr(dictArgs):
    print(coder.decodeStr(dictArgs.get('text'), dictArgs.get('key'), strOutputFile=dictArgs.get('output')))

else:
    print(coder.decodeFile(dictArgs.get('input'), dictArgs.get('key'), strOutputFile=dictArgs.get('output')))