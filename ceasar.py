#!/usr/bin/env python3

# Author: Christian Bargraser

import argparse
from argparse import RawTextHelpFormatter
import crypher.ceasar as cea

strEpilog = '''
  **************
  * UTSA - NSA *
  **************
  --- CAE-CO ---
                
'''

parser = argparse.ArgumentParser(epilog=strEpilog, formatter_class=RawTextHelpFormatter)

group_action = parser.add_mutually_exclusive_group(required=True)
group_action.add_argument('-e', '--encode', help='plaintext file')
group_action.add_argument('-d', '--decode', help='ceasar cipher encoded file')

group_shift = parser.add_mutually_exclusive_group(required=True)
group_shift.add_argument('-s', '--shift', type=int, help='number of times to shift letter (absolute value will be used)')
group_shift.add_argument('-b', '--bruteforce', help='try all combinations', action='store_true')

parser.add_argument('-o', '--output', help='output file')
dictArgs = vars(parser.parse_args())

if False == dictArgs.get('bruteforce'):

    if dictArgs.get('encode'):
        cea.encode(dictArgs.get('encode'), dictArgs.get('output'), dictArgs.get('shift'))

    else:
        cea.decode(dictArgs.get('decode'), dictArgs.get('output'), dictArgs.get('shift'))

# bruteforce
else:

    if dictArgs.get('encode'):
        strInputFile = dictArgs.get('encode')
        funcCoder = cea.encode
    
    else:
        strInputFile = dictArgs.get('decode')
        funcCoder = cea.decode

    for i in range(0, 26):
        print(f'{i:>2} ', end='')
        funcCoder(strInputFile, dictArgs.get('output'), i)
