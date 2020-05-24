#!/usr/bin/env python3

# Author: Christian Bargraser

import os
import sys
import argparse
import crypher.tap as tap
import crypher.cryparse as cyp

parser = argparse.ArgumentParser()
cyp.addCipherArgs(parser)
dictArgs = vars(parser.parse_args())

if None != dictArgs.get('input') and not os.path.isfile(dictArgs.get('input')):
    print('No such file:', dictArgs.get('input'), '\n')
    parser.print_help()
    sys.exit(1)

if cyp.isEncodeStr(dictArgs):
    print(tap.encodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))

elif cyp.isEncodeFile(dictArgs):
    print(tap.encodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))

elif cyp.isDecodeStr(dictArgs):
    print(tap.decodeStr(dictArgs.get('text'), strOutputFile=dictArgs.get('output')))

else:
    print(tap.decodeFile(dictArgs.get('input'), strOutputFile=dictArgs.get('output')))